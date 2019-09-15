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


def huffman(frequencies: List[Tuple[str, int]]):
    heap = [Leaf(value=value, char=char) for (char, value) in frequencies]
    heapq.heapify(heap)

    while len(heap) > 1:
        lf: Node = heapq.heappop(heap)
        ri: Node = heapq.heappop(heap)
        lf.code += '0'
        ri.code += '1'
        branch = Branch(value=lf.value + ri.value, lf=lf, ri=ri)
        heapq.heappush(heap, branch)
    return heap


def main():
    frequency = Counter("abacabad").most_common()
    tree = huffman(frequency)
    print(tree)


if __name__ == '__main__':
    main()
