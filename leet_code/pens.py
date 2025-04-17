def get_min_pair(n, max_pack):
    result = []
    variants: list = list(reversed(range(1, max_pack + 1)))
    print(variants)
    sum_pen = 0
    for item in variants:
        if sum_pen + item <= n:
            sum_pen += item
            result.append(item)
    return result

n = 19
max_pack = 7

print(get_min_pair(n, max_pack))
