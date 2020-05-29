import heapq
from collections import Counter, defaultdict


def huffman_encode(string):
    code_dict = defaultdict(str) if len(set(string)) > 1 else {string[0]: "0"}
    heap = [(count, char) for char, count in Counter(string).items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new = (first[0] + second[0], first[1] + second[1])
        for letter in first[1]:
            code_dict[letter] += "0"
        for letter in second[1]:
            code_dict[letter] += "1"
        heapq.heappush(heap, new)
    return code_dict


def main():
    string = input()
    code_dict = huffman_encode(string)
    encode_string = "".join([code_dict[x] for x in string])
    print(len(code_dict), len(encode_string))
    for char, code in sorted(code_dict.items()):
        print("{}: {}".format(char, code))
    print(encode_string)


if __name__ == "__main__":
    main()
