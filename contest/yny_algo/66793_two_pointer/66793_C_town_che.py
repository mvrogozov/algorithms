def count_pam(n: int, k: int, data: list[int]) -> int:
    left = 0
    right = 0
    cnt = 0
    length = len(data)
    for left in range(length):
        while (right < length) and (data[left] + k >= data[right]):
            right += 1
        if right < length and data[left] + k < data[right]:
            cnt += length - right
    return cnt

n, k = list(map(int, input().split()))
data = list(map(int, input().split()))
print(count_pam(n, k, data))


n, k = 4, 4
data = [1, 3, 5, 8]
print(data)
print(count_pam(n, k, data), '\n')

n, k = 4, 4
data = [1, 3, 5, 8, 9]
print(data)
print(count_pam(n, k, data), '\n')

n, k = 4, 4
data = [1, 3, 3, 3, 8, 8, 8]
print(data)
print(count_pam(n, k, data), '\n')