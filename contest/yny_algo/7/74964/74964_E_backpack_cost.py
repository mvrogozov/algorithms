def check():
    n, m = 5, 15
    masses = [10, 4, 2, 6, 8]
    costs = [9, 4, 2, 6, 10]
    print(get_max_cost(n, m, masses, costs))


def get_max_cost(n, m: int, masses: list[int], costs: list[int]):
    arr = [-1] * (m + 1)
    arr[0] = 0
    for item in range(n):
        pos = m - masses[item]
        while pos >= 0:
            if arr[pos] == -1:
                pos -= 1
                continue
            arr[pos + masses[item]] = max(
                arr[pos] + costs[item],
                arr[pos + masses[item]]
            )
            pos -= 1
    return max(arr)


def main():
    n, m = list(map(int, input().split()))
    masses = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(get_max_cost(n, m, masses, costs))


if __name__ == '__main__':
    main()
    # check()
