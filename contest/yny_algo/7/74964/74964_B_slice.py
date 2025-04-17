t = '3'
n = '5'
data = '1 3 3 3 2'
n = '16'
data = '1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9'
n = '7'
data = '7 2 3 4 3 2 7'


def check():
    data = [
        '1 3 3 3 2',
        '1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9',
        '7 2 3 4 3 2 7',
        '2 2',
        '3 3 3 3 3 3 3 3 3 3',
        '4 4 4 4 4 4 4 4 4 4',
        '1 1 1 1 1 1 1 1 1 1',

    ]

    for unit in data:
        print(unit)
        print(f'ans>> {get_slices(unit)}')


def get_slices(data: str):
    data = list(map(int, data.split()))
    length = 0
    res = []
    min_v = None
    for digit in data:
        if length == 0:
            min_v = digit
            length += 1
            if length == min_v:
                res.append(str(length))
                length = 0
            continue
        if digit <= length or length == min_v:
            res.append(str(length))
            length = 1
            min_v = digit
        else:
            length += 1
            min_v = min(min_v, digit)
    if length:
        res.append(str(length))
    print(len(res))
    print(' '.join(res))


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        data = input()
        get_slices(data)


if __name__ == '__main__':
    #main()
    check()
