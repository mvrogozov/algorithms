def merge_two_sorted(a: list, b: list) -> list:
    result = []
    a = list(a)
    b = list(b)
    while True:
        if a:
            if b:
                if a[0] >= b[0]:
                    result.append(b.pop(0))
                else:
                    result.append(a.pop(0))
            else:
                result.extend(a)
                break
        else:
            result.extend(b)
            break
    return result


def get_median(n: int, m: int, north: list, south: list) -> int:
    total = merge_two_sorted(north, south)
    mid = len(total) // 2
    if len(total) == 2:
        return (total[0] + total[1]) / 2
    if len(total) % 2 == 0:
        return (total[mid - 1] + total[mid]) / 2
    return total[mid]


def main():
    # a = [1, 3, 5, 7]
    # b = [2, 4, 6, 8]
    # c = [1, 2, 3]
    # d = [4, 5]
    # e = []
    # f = [1, 9]
    # print(f'a, b -> {merge_two_sorted(a, b)}')
    # print(get_median(1, 1, a, b))
    # print(f'c, d -> {merge_two_sorted(c, d)}')
    # print(get_median(1, 1, c, d))
    # print(f'e, f -> {merge_two_sorted(e, f)}')
    # print(get_median(1, 1, e, f))
    n, m = input(), input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_median(n, m, a, b))


if __name__ == '__main__':
    main()
