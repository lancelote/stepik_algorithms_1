from typing import Dict, List


def decode(string: str, codes: Dict[str, str]) -> str:
    decoded_string: List[str] = []
    current_code: List[str] = []
    for char in string:
        current_code.append(char)
        if char == "0" or (char == "1" and "1" in codes):
            decoded_string.append(codes["".join(current_code)])
            current_code = []
    if current_code:
        decoded_string.append(codes["".join(current_code)])
    return "".join(decoded_string)


def main() -> None:
    unique_letters, length = [int(x) for x in input().strip().split()]
    codes = {}
    for _ in range(unique_letters):
        char, code = input().strip().split(": ")
        codes[code] = char
    encoded_string = input().strip()
    print(decode(encoded_string, codes))


if __name__ == "__main__":
    main()
