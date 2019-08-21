from time import time


def fibonacci1(n):
    if n == 0:
        return 0

    a = 1
    b = 1
    c = a + b
    i = 3

    while i < n:
        a = b + c
        b = c + a
        c = a + b
        i += 3

    if i - n == 0:
        return c
    elif i - n == 1:
        return b
    elif i - n == 2:
        return a


def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)


def fibonacci3(n):
    if n <= 1:
        return n
    f = [0, 1]
    for i in range(1, n):
        f.append(f[i] + f[i - 1])
    return f[n]


def fibonacci4(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci5(n):
    """
    Matrix like solution with recursion
    """
    x, y = _fibonacci5(n)
    return x


def _fibonacci5(n):
    """
    Main logic for fibonacci5
    """
    if n == 0:
        return 0, 1
    else:
        a, b = _fibonacci5(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d


def fibonacci6(n):
    """
    Matrix like implementation without recursion
    """
    a = 1
    b = 0
    p = 0
    q = 1

    while n > 0:
        if n % 2 == 0:
            p, q = p*p + q*q, 2*p*q + q*q
            n //= 2
        else:
            a, b = b*q + a*q + a*p, b*p + a*q
            n -= 1
    return b


def test(n, verbose=True):
    # Algorithm №1
    t1 = time()
    result1 = fibonacci1(n)

    if verbose:
        print("Algorithm №1:", time() - t1, "sec")

    print("Result:", result1)

    # Algorithm №2
    t2 = time()
    result2 = fibonacci2(n)

    if verbose:
        print("Algorithm №2:", time() - t2, "sec")

    print("Result:", result2)

    # Algorithm №3
    t3 = time()
    result3 = fibonacci3(n)

    if verbose:
        print("Algorithm №3:", time() - t3, "sec")

    print("Result:", result3)

    # Algorithm №4
    t4 = time()
    result4 = fibonacci4(n)

    if verbose:
        print("Algorithm №4:", time() - t4, "sec")

    print("Result:", result4)


def last_n_fib(n):
    """
    Calculates last digit of the n-th fibonacci number
    """
    a = 0
    b = 1
    for i in range(n):
        a, b = b, (a + b) % 10
    return a

# Matrix wise implementation #
##############################


def matrix_multiply(a, b, m):
    return [[(a[r][0]*b[0][c] + a[r][1]*b[1][c]) %
             m for c in range(2)] for r in range(2)]


def matrix_power(a, n, m):
    if n == 0:
        return [[1 % m, 0], [0, 1 % m]]  # identity modulo m
    b = matrix_power(a, n // 2, m)
    c = matrix_multiply(b, b, m)
    if n % 2 == 1:
        c = matrix_multiply(c, a, m)
    return c


def modular_fibonacci(n, m):
    a = matrix_power([[0, 1], [1, 1]], n, m)
    return a[1][0]

print(modular_fibonacci(11527523930876953, 26673))