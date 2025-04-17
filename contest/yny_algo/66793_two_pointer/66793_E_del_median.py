def get_order(n: int, data: list):
    data.sort()
    result = []
    while data:
        length = len(data)
        mid = length // 2
        if length % 2 == 0:
            if data[mid - 1] < data[mid]:
                item = data.pop(mid -1)
            else:
                item = data.pop(mid)
        else:
            item = data.pop(mid)
        result.append(str(item))
    return ' '.join(result)

n = int(input())
data = list(map(int, input().split()))
print(get_order(n, data))



n = 4
data = [3, 3, 3, 3]
print(get_order(n, data), ' -> 3 3 3 3')
print()

n = 4
data = [3]
print(get_order(n, data), ' -> 3')
print()

n = 4
data = [19, 3]
print(get_order(n, data), ' -> 3 19')
print()

n = 4
data = [19, 3, 8]
print(get_order(n, data), ' -> 8 3 19')
print()

n = 4
data = [1, 2, 4, 2]
print(get_order(n, data), ' -> 2 2 1 4')
print()
