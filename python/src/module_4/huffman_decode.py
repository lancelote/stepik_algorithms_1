from typing import Dict, Optional


# ToDo: split Node into Branch and Leaf
class Node:
    def __init__(self, code: str, value: str = None):
        self.code = code
        self.value = value
        self.children: Optional[Dict[str, Node]] = None

    def decode(self, encoded_string: str, pos: int = 0) -> str:
        if self.value:  # Leaf
            yield self.value
        else:  # Branch
            branch = encoded_string[pos]
            yield from self.children[branch]


class Branch(Node):
    def __init__(self):
        pass


class Leaf(Node):
    def __init__(self):
        pass


class Tree:
    def __init__(self, root: Node):
        self.root = root

    @classmethod
    def from_dict(cls, decode_dict: Dict[str, str]) -> 'Tree':
        root = Node()
        for k, v in decode_dict.values():
            pass
        return Tree(root)

    def decode(self, encoded_string: str) -> str:
        return ''.join(char for char in self.root.decode(encoded_string))


def main():
    nchars, encoded_length = map(int, input().split())
    decode_dict = {}
    for _ in range(nchars):
        char, code = input().strip().split(': ')
        decode_dict[code] = char
    encoded_string = input().strip()
    tree = Tree.from_dict(decode_dict)
    print(tree.decode(encoded_string))


if __name__ == '__main__':
    main()

# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
