import sys


def main() -> None:
    scanner = sys.stdin

    line1 = next(scanner)
    _, *array = line1.split()

    line2 = next(scanner)
    _, *str_indices = line2.split()
    indices = [int(x) for x in str_indices]

    print(array)
    print(indices)


if __name__ == "__main__":
    main()
