def check():
    n, m = 5, 15
    data = [10, 4, 2, 6, 8]
    print(get_max_weight(m, data))


def get_max_weight(m: int, data: list[int]):
    arr = [-1] * (m + 1)
    arr[0] = 0
    for item in data:
        pos = m - item
        while pos >= 0:
            if arr[pos] == -1:
                pos -= 1
                continue
            arr[pos + item] = pos + item
            pos -= 1
    return max(arr)


def main():
    n, m = list(map(int, input().split()))
    data = list(map(int, input().split()))
    print(get_max_weight(m, data))


if __name__ == '__main__':
    main()
    #check()
