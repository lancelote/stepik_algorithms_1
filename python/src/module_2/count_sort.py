def count_sort(n, lst):
    """
    Enumeration sorting algorithm

    :param n: length of lst
    :type n: int
    :param lst: unordered list
    :type lst: list
    :return: ordered list
    :rtype: list
    """
    b = [0] * 11
    k = 0

    for i in range(0, n):
        b[lst[i]] += 1
    for i in range(1, 11):
        for j in range(1, b[i] + 1):
            lst[k] = i
            k += 1
    lst = [str(e) for e in lst]
    print(" ".join(lst))
