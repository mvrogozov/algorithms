def get_min_right(n: int, data: list[int]):
    stack = []
    ans = ['-1'] * n
    for i in range(n):
        if i == 0:
            stack.append((data[i], i))
            continue
        while stack and stack[-1][0] > data[i]:
            ans[stack.pop()[1]] = str(i)
        stack.append((data[i], i))
    return ' '.join(ans)


n = int(input())
data = list(map(int, input().split()))
print(get_min_right(n, data))

print()
n = 3
data = [2, 1, 3]
print(get_min_right(n, data), ' -> 1')
print()


n = 10
data = [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]
print(get_min_right(n, data), ' -> -1 4 3 4 -1 6 9 8 9 -1')
print()

n = 1
data = [1]
print(get_min_right(n, data), ' -> 1')
print()