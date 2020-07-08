def main() -> None:
    unique_letters, length = [int(x) for x in input().strip().split()]
    codes = {}
    for _ in range(unique_letters):
        char, code = input().strip().split(": ")
        codes[char] = code
    encoded_string = input().strip()


if __name__ == '__main__':
    main()
