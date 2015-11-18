import sys

data = sys.stdin.read()
line1, line2 = data.splitlines()

a = line1.split()
n = int(a[0])
del a[0]
a = [int(e) for e in a]

b = line2.split()
k = int(b[0])
del b[0]
b = [int(e) for e in b]


def binary_search(lst, value):
    """
    Binary search algorithm
    """
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r)//2
        if lst[m] > value:
            r = m - 1
        elif lst[m] < value:
            l = m + 1
        else:
            return m + 1
    return -1

result = []
for e in b:
    result.append(binary_search(a, e))
result = [str(e) for e in result]
print(" ".join(result))