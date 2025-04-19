def check():
    n = 5
    data = '2 2 2 1 5'
    k = 2
    r1 = '2 3'
    r2 = '2 5'
    r3 = '2 4'
    r4 = '4 4'

    arr = make_arr(n, data)
    pow2 = 1 << (n-1).bit_length()

    r = list(map(int, r1.split()))
    r = (r[0] - 1, r[1] - 1)
    res = get_max(0, arr, r, 0, pow2 - 1)
    print(f'{res[0]} {res[1]}')

    r = list(map(int, r2.split()))
    r = (r[0] - 1, r[1] - 1)
    res = get_max(0, arr, r, 0, pow2 - 1)
    print(f'{res[0]} {res[1]}')

    r = list(map(int, r3.split()))
    r = (r[0] - 1, r[1] - 1)
    res = get_max(0, arr, r, 0, pow2 - 1)
    print(f'{res[0]} {res[1]}')

    r = list(map(int, r4.split()))
    r = (r[0] - 1, r[1] - 1)
    res = get_max(0, arr, r, 0, pow2 - 1)
    print(f'{res[0]} {res[1]}')
    # print(get_max_index(n, data, r1), '>> ',2)
    # print(get_max_index(n, data, r2), '>> ', 5)
    # print(get_max_index(n, data, r3), '>> ', 2)
    # print(get_max_index(n, data, r4), '>> ', 1)


def get_max(n, arr, r, left, right):
    if r[0] <= left and r[1] >= right:
        return arr[n]
    if r[1] < left or r[0] > right:
        return (-1, -1)
    left_c = get_max(2 * n + 1, arr, r, left, (left + right) // 2)
    right_c = get_max(2 * n + 2, arr, r, (left + right) // 2 + 1, right)
    if left_c[0] == right_c[0]:
        return (left_c[0], left_c[1] + right_c[1])
    return max(left_c, right_c)


def make_arr(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    pow2 = 1 << (n-1).bit_length()
    data = [(v, 1) for v in data]
    arr = [(-1, -1)] * (pow2 * 2 - 1)
    arr[-pow2: -(pow2-n)] = data
    for i in range(pow2 - 2, -1, -1):
        arr[i] = max(arr[i * 2 + 1], arr[i * 2 + 2])
        v1 = arr[i * 2 + 1][0]
        v2 = arr[i * 2 + 2][0]
        c1 = arr[i * 2 + 1][1]
        c2 = arr[i * 2 + 2][1]
        if v1 == v2:
            arr[i] = (v1, c1 + c2)
    return arr


def main():
    n = int(input())
    data = input()
    k = int(input())

    arr = make_arr(n, data)
    pow2 = 1 << (n-1).bit_length()
    for _ in range(k):
        r = input()
        r = list(map(int, r.split()))
        r = (r[0] - 1, r[1] - 1)
        res = get_max(0, arr, r, 0, pow2 - 1)
        print(*res)


if __name__ == '__main__':
    main()

def main_f():
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
            print(f'{res[0]} {res[1] + 1}')

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
    #check()
