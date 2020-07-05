from __future__ import annotations

import heapq
from abc import abstractmethod, ABCMeta
from collections import Counter
from typing import List, Tuple, Optional, Dict, Iterator


class Node(metaclass=ABCMeta):
    def __init__(self, value: int = 0, code: str = "") -> None:
        self.value = value
        self.code = code

    def __gt__(self, other: None) -> bool:
        assert isinstance(other, Node)
        return self.value > other.value

    @abstractmethod
    def walk(self, code: str = "") -> Iterator[Tuple[str, str]]:
        """Walk along the tree and collect codes for each character."""
        ...


class Branch(Node):
    def __init__(self, lf: Node, ri: Node, **kwargs) -> None:
        super().__init__(**kwargs)
        self.lf = lf
        self.ri = ri

    def walk(self, code: str = "") -> Iterator[Tuple[str, str]]:
        yield from self.lf.walk(code + self.code)
        yield from self.ri.walk(code + self.code)


class Leaf(Node):
    def __init__(self, char: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.char = char

    def walk(self, code: str = "") -> Iterator[Tuple[str, str]]:
        yield self.char, code + self.code


class Tree:
    def __init__(self, root: Node, string: str) -> None:
        self.root = root
        self.string = string
        self._encode_dict = self._construct_encode_dict()

    @classmethod
    def from_string(cls, string: str) -> Tree:
        frequencies = Counter(string).most_common()
        tree = Tree(root=Tree._construct_tree(frequencies), string=string)
        return tree

    def get_encoded_string(self) -> str:
        return "".join(self._encode_dict[char] for char in self.string)

    @property
    def encode_dict_length(self) -> int:
        return len(self._encode_dict)

    def print_encode_dict(self) -> None:
        for k, v in self._encode_dict.items():
            print(f"{k}: {v}")

    @staticmethod
    def _construct_tree(frequencies: List[Tuple[str, int]]) -> Node:
        heap: List[Node] = [
            Leaf(value=value, char=char) for (char, value) in frequencies
        ]
        heapq.heapify(heap)

        if len(heap) == 1:
            heap[0].code = "0"

        while len(heap) > 1:
            lf: Node = heapq.heappop(heap)
            ri: Node = heapq.heappop(heap)
            lf.code += "0"
            ri.code += "1"
            branch = Branch(value=lf.value + ri.value, lf=lf, ri=ri)
            heapq.heappush(heap, branch)

        assert len(heap) == 1
        return heap[0]

    def _construct_encode_dict(self) -> Optional[Dict[str, str]]:
        return {char: code for (char, code) in self.root.walk()}


def main() -> None:
    string = input().strip()
    tree = Tree.from_string(string)
    encoded_string = tree.get_encoded_string()

    print(f"{tree.encode_dict_length} {len(encoded_string)}")
    tree.print_encode_dict()
    print(encoded_string)


if __name__ == "__main__":
    main()
