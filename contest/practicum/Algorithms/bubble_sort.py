def sort_bubble(arr):
    flag = False
    sorted = True
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag:
            print(*arr)
            flag = False
            sorted = False
    if sorted:
        print(*arr)
        


def main():
    input()
    arr = list(map(int, input().split()))
    sort_bubble(arr)


if __name__ == '__main__':
    main()
