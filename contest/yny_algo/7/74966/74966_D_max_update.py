def check():
    n = 5
    data = '1 2 3 4 5'
    k = 5
    #rl = ['s 1 5', 'u 3 10', 's 1 5', 'u 2 12', 's 1 3']
    rl = ['s 1 5', 'u 1 13', 's 1 5', 'u 2 12', 's 1 3']
    r1 = '2 3'
    r2 = '2 5'
    r3 = '2 4'
    r4 = '4 4'

    arr = make_arr(n, data)
    pow2 = 1 << (n-1).bit_length()
    res = []
    #rl = rl.split()
    for unit in rl:
        unit = unit.split()
        c = unit[0]
        
        if c == 's':
            r = (int(unit[1]) - 1, int(unit[2]) - 1)
            res.append(str(get_max(0, arr, r, 0, pow2 - 1)[0]))
        if c == 'u':
            r = (int(unit[1]) - 1, int(unit[2]))
            update_tree(arr, r[0], r[1])
    print(*res)
    

    # r = list(map(int, r2.split()))
    # r = (r[0] - 1, r[1] - 1)
    # res = get_max(0, arr, r, 0, pow2 - 1)
    # print(f'{res[0]} {res[1] + 1}')

    # r = list(map(int, r3.split()))
    # r = (r[0] - 1, r[1] - 1)
    # res = get_max(0, arr, r, 0, pow2 - 1)
    # print(f'{res[0]} {res[1] + 1}')

    # r = list(map(int, r4.split()))
    # r = (r[0] - 1, r[1] - 1)
    # res = get_max(0, arr, r, 0, pow2 - 1)
    # print(f'{res[0]} {res[1] + 1}')
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


def update_tree(arr, index, new_val):
    idx = len(arr) // 2 + index
    arr[idx] = (new_val, index)
    pos = (idx - 1) // 2
    while True:
        arr[pos] = max(arr[pos * 2 + 1], arr[pos * 2 + 2])
        if pos == 0:
            break
        pos = (pos - 1) // 2


def make_arr(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    pow2 = 1 << (n-1).bit_length()
    data = [(v, i) for i, v in enumerate(data)]
    arr = [(-1, -1)] * (pow2 * 2 - 1)
    arr[-pow2: -(pow2-n)] = data
    for i in range(pow2 - 2, -1, -1):
        arr[i] = max(arr[i * 2 + 1], arr[i * 2 + 2])
    return arr


def main():
    n = int(input())
    data = input()
    k = int(input())

    arr = make_arr(n, data)
    pow2 = 1 << (n-1).bit_length()
    res = []
    for _ in range(k):

        unit = input().split()
        c = unit[0]
        if c == 's':
            r = (int(unit[1]) - 1, int(unit[2]) - 1)
            res.append(str(get_max(0, arr, r, 0, pow2 - 1)[0]))
        if c == 'u':
            r = (int(unit[1]) - 1, int(unit[2]))
            update_tree(arr, r[0], r[1])
    print(*res)





def main_f():
    # n = int(input())
    # data = input()
    # k = int(input())
    #with open('D02.txt') as f:
    with open('/home/mvrogozov/Dev/exercises/contest/yny_algo/7/74966/D02.txt') as f:
        n = int(f.readline())
        data = f.readline()
        print(f'data= {data}')
        k = int(f.readline())
        arr = make_arr(n, data)
        res = []
        pow2 = 1 << (n-1).bit_length()
        for _ in range(k):
            unit = f.readline().split()
            c = unit[0]
            if c == 's':
                r = (int(unit[1]) - 1, int(unit[2]) - 1)
                res.append(str(get_max(0, arr, r, 0, pow2 - 1)[0]))
            if c == 'u':
                r = (int(unit[1]) - 1, int(unit[2]))
                update_tree(arr, r[0], r[1])
    print(*res[:10])


if __name__ == '__main__':
    #main()
    #check()
    main_f()
