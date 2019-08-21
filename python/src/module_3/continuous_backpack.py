from collections import namedtuple


def continuous_backpack(capacity, data):
    """Посчитать оптимальное наполнение ркзака добром

    Args:
        capacity (int): backpack capacity
        data (list(tuple(int, int)): (цена, вес) предмета

    Returns:
        float(): максимальная стоимость возможного наполнения, с точностью до 3
            знаков после запятой
    """
    total_value = 0
    possible_weight = capacity
    things = sorted(
        data, key=lambda x: x.price/x.weight, reverse=True
    )
    for thing in things:
        if thing.weight > possible_weight:
            total_value += possible_weight*(thing.price/thing.weight)
            break
        else:
            total_value += thing.price
            possible_weight -= thing.weight
    return round(total_value, 3)


def main():
    """Start input processing

    Returns:
        None
    """
    data = list()
    n, capacity = map(int, input().split())

    for _ in range(n):
        price, weight = map(int, input().split())
        Thing = namedtuple('Thing', ['price', 'weight'])
        data.append(Thing(price, weight))

    max_value = continuous_backpack(capacity, data)
    print(max_value)

if __name__ == '__main__':
    main()
