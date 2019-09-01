from collections import Counter
from heapq import heappush, heappop, heapify


def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def haffman_encode(text):
    """Кодирование Хаффмана

    Args:
        text (str): строка для кодировки

    Returns:
        list(int, int, dict, str): [число уникальных символов, длина
            закодированной строки, словарь {символ: код}, закодированный
            текст]
    """
    unique_chars = Counter(text)
    length = len(unique_chars)
    cipher_dct = dict()

    # Construct cipher dict
    for i in range(length):
        [(char, _)] = unique_chars.most_common(1)
        if i == length - 1 and i != 0:
            cipher_dct[char] = i*'1'
        else:
            cipher_dct[char] = i*'1' + '0'
        del unique_chars[char]

    # Encode given text
    cipher_text = ''.join([cipher_dct[char] for char in text])
    return length, len(cipher_text), cipher_dct, cipher_text


def main():
    """Start input processing

    Returns:
        None
    """
    text = input()
    unique, length, cipher_dct, encoded_text = haffman_encode(text)
    print(unique, length)
    for k, v in cipher_dct.items():
        print('%s: %s' % (k, v))
    print(encoded_text)

if __name__ == '__main__':
    main()
