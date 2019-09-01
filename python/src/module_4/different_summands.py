def different_summands(number):
    """Найти максимальное число слагаемых

    Args:
        number (int): сумма слагаемых

    Returns:
        list(int, list()): число лагаемых и их список
    """
    summand = 1
    remaining = number
    summands = []
    while True:
        if remaining == 0:
            break
        if remaining - summand < summand + 1:
            summands.append(remaining)
            break
        summands.append(summand)
        remaining -= summand
        summand += 1
    return [len(summands), summands]


def main():
    """Start input processing

    Returns:
        None
    """
    number = int(input())
    length, summands = different_summands(number)
    print(length)
    print(' '.join(map(str, summands)))

if __name__ == '__main__':
    main()
