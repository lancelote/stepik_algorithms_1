import sys
from typing import List


def bin_find(item: int, array: List[int]) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == item:
            return middle
        elif array[middle] > item:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def main() -> None:
    scanner = (map(int, line.split()) for line in sys.stdin)

    _, *array = next(scanner)
    _, *items_to_find = next(scanner)

    for item in items_to_find:
        index = bin_find(item, array)
        print(index if index == -1 else index + 1, end=" ")


if __name__ == "__main__":
    main()
