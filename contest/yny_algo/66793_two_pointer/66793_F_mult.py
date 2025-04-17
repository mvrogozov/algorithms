def get_mult(n: int, data: list):
    result = 0
    for first in range(len(data) - 2):
        for mid in range(first + 1, len(data) - 1):
            for right in range(mid + 1, len(data)):
                result += data[first] * data[mid] * data[right]
    return int(result % 1000000007)

# n = int(input())
# data = list(map(int, input().split()))
# print(get_mult(n, data))

n = 3
data = [2, 3, 4]
print(get_mult(n, data), ' -> 24')
print()

n = 3
data = [143461, 574468, 902994]
print(get_mult(n, data), ' -> 3346')
print()

n = 5
data = [10, 6, 10, 3, 7]
print(get_mult(n, data), ' -> 3346')
print()

n = 3
data = [0, 5, 6, 7]
print(get_mult(n, data), ' -> 210')
print()

n = 3
data = [1, 2, 3]
print(get_mult(n, data), ' -> 6')
print()

    # cur_mul = data[0] * data[1] * data[2]
    # result = cur_mul
    # for pos, value in enumerate(data[2:-1], start = 2):
    #     if cur_mul == 0:
    #         cur_mul = data[pos - 1] * data[pos] * data[pos + 1]
    #     else:
    #         cur_mul = data[pos + 1] * cur_mul / data[pos - 2]
    #     result += cur_mul
    # result = int(result % 1000000007)