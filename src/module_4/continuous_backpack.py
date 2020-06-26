from typing import List, NamedTuple


class Thing(NamedTuple):
    price: int
    weight: int

    @property
    def unit_cost(self) -> float:
        return self.price / self.weight


def max_value(capacity: int, data: List[Thing]) -> float:
    total_value = 0.0
    things = sorted(data, key=lambda x: x.unit_cost, reverse=True)

    for thing in things:
        weight = min(thing.weight, capacity)
        total_value += weight * thing.unit_cost
        capacity -= weight

        if capacity == 0:
            break
    return round(total_value, 3)


def main() -> None:
    data = list()
    n, capacity = [int(x) for x in input().split()]

    for _ in range(n):
        price, weight = [int(x) for x in input().split()]
        data.append(Thing(price, weight))

    print(max_value(capacity, data))


if __name__ == "__main__":
    main()
