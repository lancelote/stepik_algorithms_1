from __future__ import annotations

import heapq
from abc import abstractmethod, ABCMeta
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Generator


@dataclass
class Node(metaclass=ABCMeta):
    value: int = 0
    code: str = ''

    def __gt__(self, other: None):
        assert isinstance(other, Node)
        return self.value > other.value

    @abstractmethod
    def walk(self, code: str = '') -> Generator[Tuple[str, str], None, None]:
        ...


@dataclass
class Branch(Node):
    lf: Optional[Node] = None
    ri: Optional[Node] = None

    def walk(self, code: str = '') -> Generator[Tuple[str, str], None, None]:
        yield self.lf.walk(code + self.code)
        yield self.ri.walk(code + self.code)


@dataclass
class Leaf(Node):
    char: Optional[str] = None

    def walk(self, code: str = '') -> Generator[Tuple[str, str], None, None]:
        yield (self.char, code + self.code)


@dataclass
class Tree:
    root: Node
    string: str
    _encode_dict: Optional[Dict[str, str]] = None

    @classmethod
    def from_string(cls, string) -> Tree:
        frequency = Counter(string).most_common()
        return Tree(root=cls._construct_tree(frequency), string=string)

    @classmethod
    def _construct_tree(cls, frequencies: List[Tuple[str, int]]) -> Node:
        """Construct a huffman binary tree."""

        heap = [Leaf(value=value, char=char) for (char, value) in frequencies]
        heapq.heapify(heap)

        while len(heap) > 1:
            lf: Node = heapq.heappop(heap)
            ri: Node = heapq.heappop(heap)
            lf.code += '0'
            ri.code += '1'
            branch = Branch(value=lf.value + ri.value, lf=lf, ri=ri)
            heapq.heappush(heap, branch)
        assert len(heap) == 1
        return heap[0]

    def _construct_encode_dict(self):
        if not self._encode_dict:
            encode_dict = {char: code for (char, code) in self.root.walk()}
            self._encode_dict = encode_dict

    def encode(self):
        self._construct_encode_dict()
        return ''.join(self._encode_dict[char] for char in self.string)


def main():
    tree = Tree.from_string("abacabad")
    print(tree.encode())


if __name__ == '__main__':
    main()
