from typing import List
from typing import NamedTuple


class Section(NamedTuple):
    start: int
    end: int


def section_dot_coverage(sections: List[Section]) -> List[int]:
    sections = sorted(sections, key=lambda x: x.end)
    dots: List[int] = []

    for section in sections:
        if not dots or section.start > dots[-1]:
            dots.append(section.end)
    return dots


def main() -> None:
    data = list()
    n = int(input())

    for _ in range(n):
        start, end = [int(x) for x in input().split()]
        data.append(Section(start, end))

    dots = section_dot_coverage(data)
    print(len(dots))
    print(" ".join(str(dot) for dot in dots))


if __name__ == "__main__":
    main()
