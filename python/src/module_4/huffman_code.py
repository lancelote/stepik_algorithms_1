from __future__ import annotations

import heapq
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Node:
    value: int


@dataclass
class Branch(Node):
    lf: Node
    ri: Node


@dataclass
class Leaf(Node):
    char: str
    value: int
    code: str = ''


def huffman(frequencies: List[Tuple[str, int]]):
    heap = [Leaf(char, value) for (char, value) in frequencies]
    heapq.heapify(heap)

    while len(heap) > 1:
        lf: Node = heapq.heappop(heap)
        ri: Node = heapq.heappop(heap)
        branch = Branch(lf.value + ri.value, lf, ri)
        heapq.heappush(heap, branch)


def encode(frequency):
    print(frequency)
    heap = [[weight, [symbol, '']] for symbol, weight in frequency]
    heapq.heapify(heap)
    while len(heap) > 1:
        print(heap)
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for value in low[1:]:
            value[1] = '0' + value[1]
        for value in high[1:]:
            value[1] = '1' + value[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    print(heap)
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def main():
    frequency = Counter("abacabad").most_common()
    huff = encode(frequency)
    print(huff)


if __name__ == '__main__':
    # ToDo: try heapq + recursive approach
    main()
