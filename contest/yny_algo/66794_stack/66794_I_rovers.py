def get_timing(n: int, a: int, b: int, data: list):
    deqs = [[None] * n, [None] * n, [None] * n, [None] * n]
    starts = [0] * 4
    pntrs = [0] * 4
    ans = [None] * n
    pntr_data = 0
    ways = [1, 2, 3, 4]
    ways.remove(a)
    ways.remove(b)
    pntr_1 = pntr_2 = pntr_3 = pntr_4 = 0
    #for minute in range(n):
    minute = -1
    while True:
        if None not in ans:
            break
        minute += 1
        go_next = False
        while pntr_data < n and data[pntr_data][2] == minute + 1:
            if data[pntr_data][1] == 1:
                deqs[0][pntrs[0]] = data[pntr_data][0]
                pntrs[0] += 1

            if data[pntr_data][1] == 2:
                deqs[1][pntrs[1]] = data[pntr_data][0]
                pntrs[1] += 1

            if data[pntr_data][1] == 3:
                deqs[2][pntrs[2]] = data[pntr_data][0]
                pntrs[2] += 1

            if data[pntr_data][1] == 4:
                deqs[3][pntrs[3]] = data[pntr_data][0]
                pntrs[3] += 1
            pntr_data += 1
        if abs(a - b) == 2: #  прямая главная
            if starts[a - 1] < pntrs[a - 1]:
                ans[deqs[a - 1][starts[a - 1]] - 1] = minute + 1
                starts[a - 1] += 1
                go_next = True
            if starts[b - 1] < pntrs[b - 1]:
                ans[deqs[b - 1][starts[b - 1]] - 1] = minute + 1
                starts[b - 1] += 1
                go_next = True
            if go_next:
                continue
            if a % 2 == 0: #  left-right
                x = 0
                y = 2
            else:
                x = 1
                y = 3

            if starts[x] < pntrs[x]:
                ans[deqs[x][starts[x]] - 1] = minute + 1
                starts[x] += 1
            if starts[y] < pntrs[y]:
                ans[deqs[y][starts[y]] - 1] = minute + 1
                starts[y] += 1
        else:
            
            x, y = ways
            if b - a == 1:
                if starts[a - 1] < pntrs[a - 1]:
                    ans[deqs[a - 1][starts[a - 1]] - 1] = minute + 1
                    starts[a - 1] += 1
                    continue
                if starts[b - 1] < pntrs[b - 1]:
                    ans[deqs[b - 1][starts[b - 1]] - 1] = minute + 1
                    starts[b - 1] += 1
                    continue
            else:
                if b < a and not (b == 1 and a == 4):
                    if starts[b - 1] < pntrs[b - 1]:
                        ans[deqs[b - 1][starts[b - 1]] - 1] = minute + 1
                        starts[b - 1] += 1
                        continue
                    if starts[a - 1] < pntrs[a - 1]:
                        ans[deqs[a - 1][starts[a - 1]] - 1] = minute + 1
                        starts[a - 1] += 1
                        continue
                else:
                    if b == 4 and a == 1:
                        if starts[b - 1] < pntrs[b - 1]:
                            ans[deqs[b - 1][starts[b - 1]] - 1] = minute + 1
                            starts[b - 1] += 1
                            continue
                        if starts[a - 1] < pntrs[a - 1]:
                            ans[deqs[a - 1][starts[a - 1]] - 1] = minute + 1
                            starts[a - 1] += 1
                            continue
                    if starts[a - 1] < pntrs[a - 1]:
                        ans[deqs[a - 1][starts[a - 1]] - 1] = minute + 1
                        starts[a - 1] += 1
                        continue
                    if starts[b - 1] < pntrs[b - 1]:
                        ans[deqs[b - 1][starts[b - 1]] - 1] = minute + 1
                        starts[b - 1] += 1
                        continue

            if y - x == 1:
                if starts[x - 1] < pntrs[x - 1]:
                    ans[deqs[x - 1][starts[x - 1]] - 1] = minute + 1
                    starts[x - 1] += 1
                    continue
                if starts[y - 1] < pntrs[y - 1]:
                    ans[deqs[y - 1][starts[y - 1]] - 1] = minute + 1
                    starts[y - 1] += 1
                    continue
            else:
                if starts[y - 1] < pntrs[y - 1]:
                    ans[deqs[y - 1][starts[y - 1]] - 1] = minute + 1
                    starts[y - 1] += 1
                    continue
                if starts[x - 1] < pntrs[x - 1]:
                    ans[deqs[x - 1][starts[x - 1]] - 1] = minute + 1
                    starts[x - 1] += 1
                    continue
    return ans


# n = int(input())
# a, b = list(map(int, input().split()))
# data = []
# for i in range(n):
#     data.append([i + 1] + list(map(int, input().split())))
# data.sort(key = lambda x: x[-1])
# for i in range(n):
#     print(get_timing(n, a, b, data)[i])


# n = 27
# a, b = 4, 3
# data = [
#     [1, 4, 59],
#     [2, 4, 66],
#     [3, 3, 25],
#     [4, 3, 79],
#     [5, 2, 8],
#     [6, 4, 94],
#     [7, 2, 32],
#     [8, 1, 2],
#     [9, 3, 41],
#     [10, 1, 43],
#     [11, 2, 29],
#     [12, 4, 61],
#     [13, 4, 34],
#     [14, 2, 20],
#     [15, 3, 66],
#     [16, 3, 100],
#     [17, 3, 75],
#     [18, 3, 87],
#     [19, 2, 97],
#     [20, 1, 73],
#     [21, 3, 93],
#     [22, 1, 71],
#     [23, 1, 67],
#     [24, 3, 43],
#     [25, 2, 95],
#     [26, 2, 82],
#     [27, 2, 77],
# ]
# data.sort(key = lambda x: x[-1])
# print(data, ' -> ???')
# ans = get_timing(n, a, b, data)
# for i in range(n):
#     print(ans[i])
# print()


n = 4
a, b = 4, 1
print(a, b)
data = [
    [1, 4, 1],
    [2, 1, 1],
    [3, 1, 4],
    [4, 2, 1],

]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 2 4 3 ')
ans = get_timing(n, a, b, data)
for i in range(n):
    print(ans[i])
print()

n = 4
a, b = 1, 4
data = [
    [1, 1, 1],
    [2, 1, 2],
    [3, 3, 1],
    [4, 3, 2],

]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 2 3 4 ')
ans = get_timing(n, a, b, data)
for i in range(n):
    print(ans[i])
print()

n = 4
a, b = 1, 2
data = [
    [1, 1, 1],
    [2, 1, 2],
    [3, 3, 1],
    [4, 3, 2],

]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 2 3 4 ')
ans = get_timing(n, a, b, data)
for i in range(n):
    print(ans[i])
print()

n = 4
a, b = 3, 4
data = [
    [1, 1, 1],
    [2, 1, 2],
    [3, 3, 1],
    [4, 3, 2],
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 3 4 1 2')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()

n = 4
a, b = 3, 4
data = [
    [1, 1, 1],
    [2, 1, 2],
    [3, 3, 1],
    [4, 3, 2],
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 3 4 1 2')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()

n = 6
a, b = 3, 4
data = [
    [1, 3, 1],
    [2, 3, 2],
    [3, 3, 3],
    [4, 4, 1],
    [5, 4, 2],
    [6, 4, 3],
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 1 2 3')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()


n = 4
a, b = 1, 3
data = [
    [1, 3, 1],
    [2, 1, 2],
    [3, 2, 2],
    [4, 2, 1],
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 1 2 3')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()

n = 1
a, b = 1, 4
data = [
    [1, 1, 1],
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()


n = 5
a, b = 1, 4
data = [
    [1, 1, 4],
    [2, 1, 3],
    [3, 1, 2],
    [4, 4, 1],
    [5, 4, 2]
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 5 4 3 1 2')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()




n = 5
a, b = 1, 4
data = [
    [1, 1, 1],
    [2, 3, 1],
    [3, 2, 1],
    [4, 2, 2],
    [5, 4, 1]
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 2 5 3 4 1')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()

n = 4
a, b = 1, 2
data = [
    [1, 1, 1],
    [2, 3, 1],
    [3, 2, 1],
    [4, 2, 2]
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 4 2 3')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()

n = 4
a, b = 1, 3
data = [
    [1, 1, 1],
    [2, 3, 1],
    [3, 2, 1],
    [4, 2, 2]
]
data.sort(key = lambda x: x[-1])
print(data, ' -> 1 1 2 3')
for i in range(n):
    print(get_timing(n, a, b, data)[i])
print()


"""
12
5
1 4
1 4
1 3
1 2
4 1
4 2
4
1 3
1 1
3 1
2 1
2 2

4
1 2
1 1
2 1
3 1
4 1

1
1 4
1 1
4

1 3
3 1
1 2
2 2
2 1

6
3 4
3 1
3 2
3 3
4 1
4 2
4 3

4
3 2
1 1
1 2
3 1
3 2

4
3 4
1 1
1 2
3 1
3 2

4
1 4
1 1
1 2
3 1
3 2

4
1 2
1 1
1 2
3 1
3 2

5
1 4
2 1
1 1
4 1
3 2
3 4

27
4 3
4 59
4 66
3 25
3 79
2 8
4 94
2 32
1 2
3 41 n
1 43
2 29
4 61
4 34
2 20
3 66
3 100
3 75
3 87
2 97
1 73
3 93
1 71
1 67
3 43
2 95
2 82
2 77

ответы соответственно
5 4 3 1 2
1 1 2 3
1 2 3 4
1
1 2 4 3

1 2 3 4 5 6
3 4 1 2

3 4 1 2
1 2 3 4
1 2 3 4
3 2 1 4 5
59 67 25 79 8 94 32 2 41 44 29 61 34 20 66 100 75 87 97 73 93 71 68 43 95 82 77
"""