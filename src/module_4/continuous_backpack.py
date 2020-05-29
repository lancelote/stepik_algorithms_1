from typing import List, NamedTuple


class Thing(NamedTuple):
    price: int
    weight: int


def max_value(capacity: int, data: List[Thing]) -> float:
    total_value = 0.0
    things = sorted(data, key=lambda x: x.price / x.weight, reverse=True)

    for thing in things:
        if thing.weight > capacity:
            total_value += capacity * (thing.price / thing.weight)
            break
        else:
            total_value += thing.price
            capacity -= thing.weight
    return round(total_value, 3)


def main():
    data = list()
    n, capacity = map(int, input().split())

    for _ in range(n):
        price, weight = map(int, input().split())
        data.append(Thing(price, weight))

    print(max_value(capacity, data))


if __name__ == "__main__":
    main()
