def count_sort(arr, k):
    count_result = [0] * k
    result = []
    count = 0
    for elem in arr:
        count_result[elem] += 1
    for index, elem in enumerate(count_result):
        result[count:elem] = [index] * elem
        count += elem
    return result


def main():
    """arr = [2,1,0, 1,2,0, 0,1,2,1]"""
    input()
    arr = list(map(int, input().split()))
    arr_sorted = count_sort(arr, 3)
    print(*arr_sorted)


if __name__ == '__main__':
    main()
