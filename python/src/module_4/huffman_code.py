from __future__ import annotations

import heapq
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class Node:
    value: int = 0
    code: str = ''

    def __gt__(self, other: None):
        assert isinstance(other, Node)
        return self.value > other.value


@dataclass
class Branch(Node):
    lf: Optional[Node] = None
    ri: Optional[Node] = None


@dataclass
class Leaf(Node):
    char: Optional[str] = None


@dataclass
class Tree:
    root: Node

    @classmethod
    def from_string(cls, string) -> Tree:
        frequency = Counter(string).most_common()
        return Tree(cls.construct_tree(frequency))

    @classmethod
    def construct_tree(cls, frequencies: List[Tuple[str, int]]) -> Node:
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


def main():
    tree = Tree.from_string("abacabad")
    print(tree.root)


if __name__ == '__main__':
    main()
