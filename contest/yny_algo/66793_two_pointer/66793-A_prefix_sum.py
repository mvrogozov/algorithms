n = int(input())
data = list(map(int, input().split()))

def get_prefix_sum(data: list) -> list:
    result = []
    for pos, item in enumerate(data):
        if pos == 0:
            result.append(item)
            continue
        result.append(result[pos - 1] + item)
    return result

for item in get_prefix_sum(data):
    print(item, end=' ')

tdata = [2, 3, 4, 5, 6, 7, 8]
print(tdata)
print(get_prefix_sum(tdata))
print()


tdata = [-2, -3, -4, -5, -6, 7, 8]
print(tdata)
print(get_prefix_sum(tdata))
