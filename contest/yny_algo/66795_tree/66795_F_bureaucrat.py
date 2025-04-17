import time
import sys
sys.setrecursionlimit(10000000)


# def count_coins(n: int, data: list[str]):
#     data = list(map(int, data[0].split()))
#     # print(f'{n} -> {data}')
#     node_childs: dict[int, list[int]] = {}
#     ans = [0] * n
#     for i, boss in enumerate(data, start=2):
#         boss_empls = node_childs.setdefault(boss, [])
#         node_childs.setdefault(i, [])
#         boss_empls.append(i)

#     for _ in range(n):
#         go_down_and_delete(1, 1, node_childs, ans)
#     print(*ans)


def go_down_and_delete(
    top: int,
    come_from: int,
    node_childs: dict[int, list[int]],
    ans: list[int]
):
    coins = 1
    if not node_childs[top]:
        ans[top - 1] += coins
        if node_childs[come_from]:
            node_childs[come_from].pop(0)
        return coins
    coins += go_down_and_delete(node_childs[top][0], top, node_childs, ans)
    ans[top - 1] += coins
    return coins


def count_coins(n: int, data: list[str]):
    data = list(map(int, data[0].split()))
    # print(f'{n} -> {data}')
    node_childs: dict[int, list[int]] = {}
    ans = [0] * n
    for i, boss in enumerate(data, start=2):
        boss_empls = node_childs.setdefault(boss, [])
        node_childs.setdefault(i, [])
        boss_empls.append(i)

    get_coins_and_depth(1, node_childs, ans)
    print(*ans)


def get_coins_and_depth(
    top: int,
    node_childs: dict[int, list[int]],
    ans: list[int],
):
    coins = 0
    cnt = 1
    if not node_childs[top]:
        ans[top - 1] = 1
        return 1, cnt
    for child in node_childs[top]:
        in_coins, in_cnt = get_coins_and_depth(
            child,
            node_childs,
            ans
        )
        cnt += in_cnt
        coins += in_coins
    coins += cnt
    ans[top - 1] += coins
    return coins, cnt

t1 = time.time()

with open('input.txt') as f:
    n = int(f.readline())
    data = f.read().splitlines()
pointers = [0] * n
count_coins(n, data)

print(time.time() - t1)
# n = 33
# pointers = [0] * n
# data = ['1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32']
# count_coins(n, data)

# n = 5
# data = ['1 2 2 4']
# count_coins(n, data)
