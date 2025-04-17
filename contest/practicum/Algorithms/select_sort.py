def sort_select(arr):
    pos = 0
    for i in range(len(arr)):
        min_el = arr[i]
        pos = i
        for j in range(i, len(arr)):
            if arr[j] < min_el:
                min_el = arr[j]
                pos = j
        if pos != i:
            arr[i], arr[pos] = arr[pos], arr[i]
            print(*arr)
    print('result= ', *arr)


def main():
    arr = [11, 2, 9, 7, 1]
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_select(arr)


if __name__ == '__main__':
    main()