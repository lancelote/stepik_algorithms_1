def fib_digit(n):
    """Find given Fibonacci number last digit."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a + b) % 10
    return a


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
