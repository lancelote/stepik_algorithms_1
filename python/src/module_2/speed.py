import math


def f1(n):
    return 3**math.log(n, 2)


def f2(n):
    return n**math.log(n, 2)


def f3(n):
    return 2**n


def f4(n):
    return 4**n


def f5(n):
    return math.log(n, 3)


def f6(n):
    return math.sqrt(n)


def f7(n):
    return math.log(math.factorial(n), 2)


def f8(n):
    return n**2


def f9(n):
    return 7**math.log(n, 2)


def f10(n):
    return 2**(2**n)


def f11(n):
    return math.log(math.log(n, 2), 2)


def f12(n):
    return (math.log(n, 2))**2


def f13(n):
    return (math.log(n, 2))**(math.log(n, 2))


def f14(n):
    return math.sqrt(math.log(n, 4))


def f15(n):
    return n/(math.log(n, 5))


def f16(n):
    return math.factorial(n)


def f17(n):
    return n**(math.sqrt(n))


def test(n):
    #print("1 :", int(f1(n)))
    #print("2 :", int(f2(n)))
    #print("3 :", int(f3(n)))
    #print("4 :", int(f4(n)))
    #print("5 :", int(f5(n)))
    #print("6 :", int(f6(n)))
    #print("7 :", int(f7(n)))
    #print("8 :", int(f8(n)))
    #print("9 :", int(f9(n)))
    #print("10 :", int(f10(n)))
    print("11 :", int(f11(n)))
    #print("12 :", int(f12(n)))
    #print("13 :", int(f13(n)))
    print("14 :", int(f14(n)))
    #print("15 :", int(f15(n)))
    #print("16 :", int(f16(n)))
    #print("17 :", int(f17(n)))

test(10**50)