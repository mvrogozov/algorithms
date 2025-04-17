def check():
    n, m = 5, 15
    masses = [10, 4, 2, 6, 8]
    costs = [9, 4, 2, 6, 10]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m}')
    print()

    n, m = 4, 6
    masses = [2, 4, 1, 2]
    costs = [7, 2, 5, 1]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m} right= 4 3 1')
    print()

    n, m = 2, 789
    masses = [45, 44, 44, 20]
    costs = [51, 41, 40, 40]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m}')
    print()
    print('#################')

    n, m = 92, 724
    masses = [30,30,25,24,25,7,9,32,17,3,14,22,29,31,25,18,6,29,7,7,34,6,12,11,13,23,3,18,34,3,20,6,18,21,11,14,33,21,14,6,5,7,19,26,30,24,8,4,1,14,5,18,30,28,10,25,15,2,4,22,4,28,28,28,23,21,23,28,3,30,15,33,10,4,15,34,18,5,14,17,21,17,1,26,2,8,8,25,8,14,9,16]
    costs =  [52,10,41,69,82,5,21,18,39,48,87,15,82,66,67,18,84,71,94,82,67,73,67,90,67,85,68,25,3,65,55,95,56,21,91,58,90,65,43,59,83,35,73,95,60,43,27,92,38,86,58,25,10,30,65,33,77,58,32,2,37,89,56,47,5,13,95,75,94,59,72,2,25,43,49,9,60,19,2,69,90,61,7,71,36,40,38,23,45,35,39,6]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m}')
    print()

    print()
    n, m = 4, 90
    masses = [30, 30, 25, 24]
    costs = [52, 10, 41, 69]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m}')
    print()

    n, m = 2, 27
    masses = [30, 35]
    costs = [3, 9]
    res = get_unit_nums(n, m, masses, costs)
    print(res)
    mas = total = 0
    for i in res:
        mas += masses[i - 1]
        total += costs[i - 1]
    print(f'm={mas}, cost = {total}, maxm={m}')
    print()


def get_unit_nums(n, m: int, masses: list[int], costs: list[int]):
    matrix = []
    for item in range(n):
        if not item:
            arr = [(-1, -1)] * (m + 1)
            arr[0] = (0, 0)
        else:
            arr = list(matrix[item - 1])
        pos = m - masses[item]
        while pos >= 0:
            if arr[pos] == (-1, -1):
                pos -= 1
                continue
            if arr[pos][0] + costs[item] > arr[pos + masses[item]][0]:
                arr[pos + masses[item]] = (arr[pos][0] + costs[item], item)
            pos -= 1
        # print(f'arr = {arr[44:47]}', end=' >>')
        # print(f'arr = {arr[85:90]} {arr[127:135]}')
        # deb_max = max(arr, key=lambda x: x[1])
        # print(f'item = {item} maxrow = {deb_max}')
        matrix.append(arr)
    #print(matrix[0:-1][40:52])
    
    unit = (0, 0)
    elem_pos = 0
    for pos, item in enumerate(matrix[-1]):
        if item[0] > unit[0]:
            unit = item
            elem_pos = pos
    res = []
    row = len(matrix) - 1
    #print(f'pos = {elem_pos}, unit = {unit}')
    #print(matrix)
    while row >= 0:
        if unit == (0, 0):
            break
        #print(f'append {unit}->{unit[1] + 1} in row = {row}')
        res.append(unit[1] + 1)
        elem_pos = elem_pos - masses[unit[1]]
        row = unit[1] - 1
        unit = matrix[row][elem_pos]

    return res


def main():
    n, m = list(map(int, input().split()))
    masses = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(' '.join(list(map(str, get_unit_nums(n, m, masses, costs)))))
    for row in get_unit_nums(n, m, masses, costs):
        print(row)


if __name__ == '__main__':
    #main()
    check()
