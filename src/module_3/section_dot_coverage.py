def section_dot_coverage(sections):
    """Покрыть отрезки точками

    Args:
        sections (list(tuple(int, int)): список отрезков

    Returns:
        list(int, list())
    """
    sections = sorted(sections, key=lambda x: x[1])
    dots = []

    for section in sections:
        if len(dots) == 0 or section[0] > dots[-1]:
            dots.append(section[1])

    return [len(dots), dots]


def main():
    """Start input processing

    Returns:
        None
    """
    data = list()
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        data.append((a, b))

    length, dots = section_dot_coverage(data)
    print(length)
    print(' '.join(map(str, dots)))

if __name__ == '__main__':
    main()
