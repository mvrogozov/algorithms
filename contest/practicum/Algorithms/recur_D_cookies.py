def get_happy_kid(n: int, fz: list, m: int, cs: list) -> int:
    result = 0
    cs.sort(reverse=True)
    fz.sort()
    for kid_z in fz:
        while cs:
            cookie = cs.pop()
            if kid_z <= cookie:
                result += 1
                break
    return result


def main():
    n = 10
    fz = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7]
    m = 8
    cs = [9, 8, 1, 1, 1, 5, 10, 8]
    # n = int(input())
    # fz = list(map(int, input().split()))
    # m = input()
    # cs = list(map(int, input().split()))
    print(get_happy_kid(n, fz, m, cs))


if __name__ == '__main__':
    main()
