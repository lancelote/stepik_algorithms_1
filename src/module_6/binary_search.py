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
    scanner = sys.stdin

    line1 = next(scanner)
    _, *raw_array = line1.split()
    array = [int(x) for x in raw_array]

    line2 = next(scanner)
    _, *raw_items_to_find = line2.split()
    items_to_find = [int(x) for x in raw_items_to_find]

    for item in items_to_find:
        index = bin_find(item, array)
        print(index if index == -1 else index + 1, end=" ")


if __name__ == "__main__":
    main()
