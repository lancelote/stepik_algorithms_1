def fibonacci(n):
    """Calculate the given Fibonacci number."""
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
