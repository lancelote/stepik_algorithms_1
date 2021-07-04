from __future__ import annotations

from collections import deque
from typing import Deque
from typing import Dict


class Node:
    def __init__(self):
        self.char: str | None = None
        self.left: Node | None = None
        self.right: Node | None = None

    @staticmethod
    def from_codes(codes: Dict[str, Deque[str]]) -> Node:
        root = Node()

        for char, code in codes.items():
            root.parse(char, code)

        return root

    def get_left(self) -> Node:
        if self.left is None:
            left = self.left = Node()
        else:
            left = self.left
        return left

    def get_right(self) -> Node:
        if self.right is None:
            right = self.right = Node()
        else:
            right = self.right
        return right

    def parse(self, char: str, code: Deque[str]) -> None:
        if not code:
            self.char = char
        else:
            if code.popleft() == "0":
                child = self.get_left()
            else:
                child = self.get_right()
            child.parse(char, code)

    def decode(self, code: str) -> str:
        result = []
        current = self

        for digit in code:
            if digit == "0":
                current = current.get_left()
            else:
                current = current.get_right()

            if current.char:
                result.append(current.char)
                current = self

        return "".join(result)


def main() -> None:
    unique_letters, length = [int(x) for x in input().strip().split()]
    codes = {}
    for _ in range(unique_letters):
        char, code = input().strip().split(": ")
        codes[char] = deque(code)
    encoded_string = input().strip()
    tree = Node.from_codes(codes)
    print(tree.decode(encoded_string))


if __name__ == "__main__":
    main()
