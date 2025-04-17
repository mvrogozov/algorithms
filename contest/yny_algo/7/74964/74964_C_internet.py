def check():
    n = 11
    data = '1 1 10 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
    print(int(get_total_money(n, data)), '==5')

    n = 11
    data = '3 2 10 1'
    print(get_total_money(n, data), '== 4')

    n = 100
    data = '1 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100'
    print(get_total_money(n, data), '== 2')
    n = 45
    data = '1 1 3 12 24 22 56 101 300 559 2 620 315 219 491 863 579 144 802 61 615 279 137 277 981 666 647 305 686 843 224'
    print(get_total_money(n, data),'== 32')

    n = 11
    data = '1'
    print(get_total_money(n, data), '== 11')

    n = 11
    data = '4 5'
    print(get_total_money(n, data), '== 3')

    n = 6
    data = '1413434332545323'
    print(get_total_money(n, data), '== 1')

    n = 999999999
    data = '1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608 16777216 33554432 67108864 134217728 268435456 536870913 73741824'
    print(get_total_money(n, data), '== 3')

    n = 123
    data = '1 3 5 9 17 33 65 129 201 418 878 383 319 703 924 787 454 979 655 791 566 321 306 169 888 479 905 259 433 53 428'
    print(get_total_money(n, data), '== 82')

    n = 89345
    data = '1 1 5 4 2 50 40 1 507 334 655 326 297 17836 23732 20155 200851 71049 261512 740443 1128188 2753884 2165268 7900933 3313262 1080515 7368817 5069318 2506005 5300223 6978145'
    print(get_total_money(n, data), '== 3?')

def get_total_money2(n: int, data: str):
    data: list[int] = list(map(int, data.split()))
    arr = [-1] * (n + 1)
    # arr = [-1] * max((max(data) * 2 + 1), n * 2)
    length = len(arr)
    best = None
    arr[0] = 0
    different_seconds = set()
    for pos, sec in enumerate(data):
        if sec in different_seconds:
            continue
        exit_flag = False
        for item in different_seconds:
            if sec % item == 0 or item % sec == 0:
                exit_flag = True
                break
        different_seconds.add(sec)
        if exit_flag:
            continue
        for total, val in enumerate(arr):
            if total > n:
                break
            if val == -1:
                continue
            if (
                (sec + total <= n) and
                (
                    (arr[sec + total] > val + 2 ** pos) or
                    (arr[sec + total] == -1)
                )
            ):
                arr[sec + total] = val + 2 ** pos
            elif (
                sec + total > n
            ):
                if not best:
                    best = val + 2 ** pos
                best = min(best, val + 2 ** pos)
        #print(f'pos={pos} sec={sec} arr={arr[n:n+20]}')
    res = arr[n]
    if best:
        if res == -1:
            res = best
        else:
            res = min(res, best)
    else:
        res = min(res)
    return res


def get_total_money(n: int, data: str):
    data: list[int] = list(map(int, data.split()))
    best_prices = []
    for pos, seconds in enumerate(data):
        # rub/sec, rub, sec
        best_prices.append((seconds / 2 ** pos, 2 ** pos, seconds))
    best_prices.sort(reverse=True)
    uniq_min = set()
    for bp in best_prices:
        is_mult = False
        for um in tuple(uniq_min):
            if bp[0] == um[0]:
                if bp[2] % um[2] == 0:
                    is_mult = True
                    break
                if um[2] % bp[2] == 0:
                    uniq_min.remove(um)
                    uniq_min.add(bp)
        if not is_mult:
            uniq_min.add(bp)

    uniq_min = sorted(list(uniq_min))
    #print(f'uniq bp = {uniq_min}')

    #print(f'best prices= {best_prices[:10]}')
    total_sec = 0
    res = 0
    cur_best_price = None
    while uniq_min:
        unit = uniq_min.pop()
        cards_amount = n / unit[2]
        remain_amount = n - total_sec

        if cards_amount == 1:
            if cur_best_price:
                if unit[1] < cur_best_price:
                    return unit[1]
            else:
                return unit[1]

        # если секунд в карточке больше
        if cards_amount < 1:
            cur_best_price = (
                min(unit[1], cur_best_price) if cur_best_price else unit[1]
            )
            continue

        cards_to_goal = remain_amount / unit[2]
        if cards_to_goal == int(cards_to_goal):
            if cur_best_price:
                return min(cur_best_price, res + cards_to_goal * unit[1])
            return res + cards_to_goal * unit[1]
        # if cards_to_goal == 1:
        #     if unit[1] < cur_best_price:
        #         return unit[1] + res
        elif cards_to_goal < 1: # если перебор
            cur_best_price = (
                min(res + unit[1], cur_best_price) if
                cur_best_price else res + unit[1]
            )
            continue
        else:
            total_sec += unit[2] * int(cards_to_goal)
            res += unit[1] * int(cards_to_goal)
            cur_best_price = (
                min(res + unit[1], cur_best_price) if
                cur_best_price else res + unit[1]
            )
    return cur_best_price


def main():
    n = int(input())
    data = input()
    print(int(get_total_money(n, data)))


if __name__ == '__main__':
    #main()
    check()
