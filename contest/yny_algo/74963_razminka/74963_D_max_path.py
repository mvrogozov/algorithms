def make_graph(data: list[str]):
    w = len(data[0].split()) - 1
    h = len(data) - 1
    res: dict = {}
    cost_matrix: dict = {}
    for r_num, row in enumerate(data):
        for c_num, digit in enumerate(list(map(int, row.split()))):
            routes: list = res.setdefault((r_num, c_num), [])
            cost_matrix[(r_num, c_num)] = digit
            if r_num < h:
                routes.append((r_num + 1, c_num))
            else:
                routes.append(None)
            if c_num < w:
                routes.append((r_num, c_num + 1))
            else:
                routes.append(None)
    return res, cost_matrix


def go_through(cur_point, routes, cur_sum, cost_matrix, cur_path):
    global max_sum
    global best_path
    if routes.get(cur_point) == [None, None]:  # last step
        cur_sum += cost_matrix.get(cur_point)
        if cur_sum > max_sum:
            max_sum = cur_sum
            best_path = cur_path
        # print(f'SUM in {cur_point} = {cur_sum}')
    for direction, next_point in enumerate(routes.get(cur_point)):
        if next_point is None:
            continue
        if direction == 0:
            # print(f'from {cur_point} going down to {next_point}')
            cur_path += 'D '
        else:
            # print(f'from {cur_point} going right to {next_point}')
            cur_path += 'R '
        new_sum = cur_sum + cost_matrix.get(cur_point)
        go_through(next_point, routes, new_sum, cost_matrix, cur_path)
        cur_path = cur_path[:-2]


def main():
    data = [
        '9 9 9 9 9',
        '3 0 0 0 0',
        '9 9 9 9 9',
        '6 6 6 6 8',
        '9 9 9 9 9'
    ]
    n, m = (map(int, input().split()))
    data = []
    for i in range(n):
        data.append(input())
    global max_sum
    global best_path
    best_path = ''
    max_sum = 0
    #print('start')
    paths, cost_matrix = make_graph(data)
    # for k, v in paths.items():
    #     print(f'{k}: {v}')
    go_through((0, 0), paths, 0, cost_matrix, cur_path='')
    print(max_sum)
    if best_path:
        print(best_path.strip())


if __name__ == '__main__':
    main()
