from typing import List


def different_summands(number: int) -> List[int]:
    """Find unique int summands of a given number."""
    summand = 1
    remaining = number
    summands = []

    while remaining:
        # If after a summand subtraction we will end up with a number which is
        # less or equal to summand itself we will be stuck as the remaining
        # part can not be expressed with new unique summands so we have to stop
        # here and simply add remaining part as one big summand
        if remaining - summand <= summand:
            summands.append(remaining)
            break

        summands.append(summand)
        remaining -= summand
        summand += 1
    return summands


def main() -> None:
    number = int(input())
    summands = different_summands(number)
    print(len(summands))
    print(" ".join(str(x) for x in summands))


if __name__ == "__main__":
    main()
