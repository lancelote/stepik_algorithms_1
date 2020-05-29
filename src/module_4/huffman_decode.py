from abc import ABCMeta, abstractmethod
from typing import Dict


class Node(metaclass=ABCMeta):
    @abstractmethod
    def decode(self, encoded_string: str, pos: int) -> str:
        ...


class Branch(Node):
    def __init__(self, lf: Node, ri: Node):
        self.children = {"0": lf, "1": ri}

    def decode(self, encoded_string: str, pos: int) -> str:
        code = encoded_string[pos]
        yield from self.children[code].decode(encoded_string, pos + 1)


class Leaf(Node):
    def __init__(self, char: str):
        self.char = char

    def decode(self, encoded_string: str, pos: int) -> str:
        yield self.char


class Tree:
    def __init__(self, root: Node):
        self.root = root

    @classmethod
    def from_dict(cls, decode_dict: Dict[str, str]) -> "Tree":
        root = Branch()
        for k, v in decode_dict.values():
            pass
        return Tree(root)

    def decode(self, encoded_string: str) -> str:
        return "".join(char for char in self.root.decode(encoded_string))


def main():
    nchars, encoded_length = map(int, input().split())
    decode_dict = {}
    for _ in range(nchars):
        char, code = input().strip().split(": ")
        decode_dict[code] = char
    encoded_string = input().strip()
    tree = Tree.from_dict(decode_dict)
    print(tree.decode(encoded_string))


if __name__ == "__main__":
    main()
