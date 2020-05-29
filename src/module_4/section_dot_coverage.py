from typing import Tuple, List

Section = Tuple[int, int]


def section_dot_coverage(sections: List[Tuple]) -> List[int]:
    sections = sorted(sections, key=lambda x: x[1])
    dots: List[int] = []

    for section in sections:
        if not dots or section[0] > dots[-1]:
            dots.append(section[1])
    return dots


def main():
    data = list()
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        data.append((a, b))

    dots = section_dot_coverage(data)
    print(len(dots))
    print(" ".join(map(str, dots)))


if __name__ == "__main__":
    main()
