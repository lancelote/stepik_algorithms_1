import sys
from typing import List


class Heap:
    def __init__(self) -> None:
        self.data: List[int] = []

    def insert(self, item: int) -> None:
        self.data.append(item)
        i = len(self) - 1
        parent = (i - 1) // 2

        while i > 0 and self.data[parent] < self.data[i]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
            parent = (i - 1) // 2

    def extract_max(self) -> int:
        assert len(self) > 0, "no more elements"

        result = self.data[0]
        if len(self) == 1:
            self.data.pop()
        else:
            self.data[0] = self.data.pop()
            self.heapify(0)
        return result

    def heapify(self, i) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < len(self) and self.data[left] > self.data[largest]:
                largest = left

            if right < len(self) and self.data[right] > self.data[largest]:
                largest = right

            if largest == i:
                break

            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def __len__(self):
        return len(self.data)


def main():
    heap = Heap()
    _ = input()

    for line in sys.stdin:
        if line.startswith("Insert"):
            _, value = line.split()
            heap.insert(int(value))
        elif line.startswith("ExtractMax"):
            print(heap.extract_max())
        else:
            raise ValueError(f"unknown command {line}")


if __name__ == "__main__":
    main()
