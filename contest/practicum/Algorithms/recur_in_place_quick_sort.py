# 68704019
def is_better(first, second):
    if first[1] == second[1]:
        if first[2] == second[2]:
            return first[0] <= second[0]
        return first[2] < second[2]
    return first[1] > second[1]


def in_place_quick_sort(arr):
    length = len(arr)
    left = 0
    right = length - 1
    if length <= 1:
        return arr
    if length == 2:
        if is_better(arr[right], arr[left]):
            arr[left], arr[right] = arr[right], arr[left]
        return arr
    mid = (right - left) // 2
    pivot = arr[mid]
    while left < right:
        if is_better(arr[left], pivot):
            left += 1
        if is_better(pivot, arr[right]):
            right -= 1
        if left >= right:
            break
        if (
            is_better(pivot, arr[left])
            and
            is_better(arr[right], pivot)
        ):
            arr[left], arr[right] = (
                arr[right], arr[left]
            )
            left += 1
            right -= 1
    arr[0:left + 1] = in_place_quick_sort(arr[0:left + 1])
    arr[left:length] = in_place_quick_sort(arr[left:length])
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = [None] * n
    for i in range(n):
        in_data = list(input().split())
        arr[i] = in_data
        arr[i][0] = in_data[0]
        arr[i][1] = int(in_data[1])
        arr[i][2] = int(in_data[2])
    arr = in_place_quick_sort(arr)
    result = ''
    for elem in arr:
        result += elem[0] + '\n'
    print(result)
