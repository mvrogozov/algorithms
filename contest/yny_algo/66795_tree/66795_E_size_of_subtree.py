import sys
sys.setrecursionlimit(100000)


def get_all_sizes(n: int, data: list):
    #print(n, ' -> ', data)
    node_childs: dict[int, list[int]] = {}
    ans = [None] * n
    for pair in data:
        n1, n2 = list(map(int, pair.split()))
        n1_c = node_childs.setdefault(n1, [])
        n2_c = node_childs.setdefault(n2, [])
        n1_c.append(n2)
        n2_c.append(n1)
    print(node_childs)
    count_nodes(1, 1, node_childs, ans)
    print(*ans)


def count_nodes(top: int, come_from: int, node_childs: dict[int, list[int]], cache: list[int]):
    cnt = 1
    for child in node_childs[top]:
        if child == come_from:
            continue
        cnt += count_nodes(child, top, node_childs, cache)
    cache[top - 1] = cnt
    return cnt


# n = 5
# data = ['1 4', '3 4', '5 2', '5 4']

with open('input.txt') as f:
    n = int(f.readline())
    data = f.read().splitlines()
get_all_sizes(n, data)
