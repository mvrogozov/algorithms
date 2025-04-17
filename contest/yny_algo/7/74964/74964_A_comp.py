def check():
    data1 = '1 1'
    data2 = '2 3 1'
    data3 = '2 5 4 3'

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    assert count_groups(x, y) == ('3 2 4', 3), '1'

    data1 = '1 1'
    data2 = '1'
    data3 = '2'

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    assert count_groups(x, y) == ('1', 1), '2'

    data1 = '1 1'
    data2 = '1'
    data3 = '1'

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    assert count_groups(x, y) == ('0', 0), '3'

    data1 = '1 1'
    data2 = '2 2 3 3'
    data3 = '3 2 4 5'

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    assert count_groups(x, y) == ('1 0 4 3', 3), '4'

    print('>>>>>>>5')
    data1 = '2 2'
    data2 = '1 2'
    data3 = '2 3'

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    assert count_groups(x, y) == ('1 2', 2), '5'

    count_groups(x, y)

def count_groups(x: list[int], y: list[int]):
    groups = []
    rooms = []
    for pos, val in enumerate(x, start=1):
        groups.append((pos, val))
    for pos, val in enumerate(y, start=1):
        rooms.append((pos, val))
    groups.sort(key=lambda x: x[1], reverse=True)
    rooms.sort(key=lambda x: x[1])
    res = []
    amount = 0
    room = rooms.pop()
    for group in groups:
        if room[1] > group[1]:
            res.append((group[0], room[0]))
            amount += 1
            if rooms:
                room = rooms.pop()
        else:
            res.append((group[0], 0))
    res.sort()
    res = ' '.join([str(g[1]) for g in res])
    print(amount)
    print(res)
    return res, amount


def main():

    data1 = input()
    data2 = input()
    data3 = input()

    n, m = list(map(int, data1.split()))
    x = list(map(int, data2.split()))
    y = list(map(int, data3.split()))

    count_groups(x, y)


if __name__ == '__main__':
    main()
    # check()
