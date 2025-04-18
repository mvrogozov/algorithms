def check():
    n = 5
    data = '2 2 2 1 5'
    k = 2
    r1 = '2 3'
    r2 = '2 5'
    r3 = '2 4'
    r4 = '4 4'
    # print(get_max_index(n, data, r1), '>> ',2)
    # print(get_max_index(n, data, r2), '>> ', 5)
    # print(get_max_index(n, data, r3), '>> ', 2)
    # print(get_max_index(n, data, r4), '>> ', 1)


def get_max(n, arr, r, left, right):
    if r[0] <= left and r[1] >= right:
        return arr[n]
    if r[1] < left or r[0] > right:
        return (-1, -1)
    return max(
        get_max(2 * n + 1, arr, r, left, (left + right) // 2),
        get_max(2 * n + 2, arr, r, (left + right) // 2 + 1, right)
    )


def make_arr(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    pow2 = 1 << (n-1).bit_length()
    data = [(v, i) for i, v in enumerate(data)]
    arr = [(-1, -1)] * (pow2 * 2 - 1)
    arr[-pow2: -(pow2-n)] = data
    for i in range(pow2 - 2, -1, -1):
        arr[i] = max(arr[i * 2 + 1], arr[i * 2 + 2])
    # [5, 2, 5, 2, 2, 5, -1, 2, 2, 2, 1, 5, -1, -1, -1]

    return arr


def main():
    # n = int(input())
    # data = input()
    # k = int(input())
    with open('10.txt') as f:
        n = int(f.readline())
        data = f.readline()
        k = int(f.readline())
        arr = make_arr(n, data)
        pow2 = 1 << (n-1).bit_length()
        for _ in range(k):
            r = f.readline()
            r = list(map(int, r.split()))
            r = (r[0] - 1, r[1] - 1)
            res = get_max(0, arr, r, 0, pow2 - 1)
            print(f'{res[1] + 1}')

    # arr = make_arr(n, data)
    # pow2 = 1 << (n-1).bit_length()
    # for _ in range(k):
    #     r = input()
    #     r = list(map(int, r.split()))
    #     r = (r[0] - 1, r[1] - 1)
    #     res = get_max(0, arr, r, 0, pow2 - 1)
    #     print(f'{res[1] + 1}')


if __name__ == '__main__':
    main()
