n = 4
arr = [1, 0, 2, 3, 4]

arr2 = [3, 6, 7, 4, 1, 5, 0, 2]

# n = int(input())
# arr = list(map(int, input().split()))
arr3 = [12, 1, 8, 0, 7, 17, 2, 20, 9, 19, 18, 6, 14, 21, 10, 4, 23, 5, 3, 15, 13, 11, 22, 16]


def get_max_blocks(arr) -> int:
    zero_index = arr.index(0)
    start_index = zero_index + 1
    if zero_index == len(arr) - 1:
        return 1
    blocks_indexes = [start_index]
    while start_index < len(arr):
        #for num in range(start_index + 1, len(arr)):
        right_min = min(arr[start_index:])
        if max(arr[:start_index]) < right_min:
            blocks_indexes.append(start_index)
        start_index = arr.index(right_min) + 1
    return len(blocks_indexes)


def main():
    print(get_max_blocks(arr))
    print(get_max_blocks(arr2))
    print(get_max_blocks(arr3))


if __name__ == '__main__':
    main()
