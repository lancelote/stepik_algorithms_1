def fib_mod(n: int, m: int) -> int:
    modules = [0, 1]
    i = 2

    while not (modules[i - 2] == 0 and modules[i - 1] == 1) or i <= 2:
        modules.append((modules[i - 2] + modules[i - 1]) % m)
        i += 1

    return modules[n % (i - 2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
