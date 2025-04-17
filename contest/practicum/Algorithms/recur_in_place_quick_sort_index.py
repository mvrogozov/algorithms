# 68687416
def is_better(first, second):
    if first[1] == second[1]:
        if first[2] == second[2]:
            return first[0] <= second[0]
        return first[2] < second[2]
    return first[1] > second[1]


def in_place_quick_sort_index(arr, left, right):
    if right - left < 1:
        return
    if right - left == 1:
        if is_better(arr[right], arr[left]):
            arr[left], arr[right] = arr[right], arr[left]
        return
    mid = left + (right - left) // 2
    pivot = arr[mid]
    left_index = left
    right_index = right
    while left_index < right_index:
        if is_better(arr[left_index], pivot):
            left_index += 1
        if is_better(pivot, arr[right_index]):
            right_index -= 1
        if left_index >= right_index:
            break
        if (
            is_better(pivot, arr[left_index])
            and is_better(arr[right_index], pivot)
        ):
            arr[left_index], arr[right_index] = (
                arr[right_index], arr[left_index]
            )
            left_index += 1
            right_index -= 1
    in_place_quick_sort_index(arr, left, left_index)
    in_place_quick_sort_index(arr, left_index, right)
    return arr


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
    arr = (
        in_place_quick_sort(arr[0:left]) +
        in_place_quick_sort(arr[left:length])
    )
    return arr


if __name__ == '__main__':

    arr = [
        ['alla', 4, 100],
        ['gena', 6, 1000],
        ['gosha', 2, 90],
        ['rita', 2, 90],
        ['timofey', 4, 80]
    ]

    arr = [
        ['alla', 0, 0],
        ['gena', 0, 0],
        ['gosha', 0, 0],
        ['rita', 0, 0],
        ['timofey', 0, 0]
    ]


    arr = [
        ['ixetulueozem 55', 55, 26],
        ['edrnkztanvrpyjvso 65', 65, 7],
        ['e', 89, 9],
        ['ayrcrulcwh 99', 99, 14],
        ['nsgnysqm 15', 15, 32],
        ['ewdponbpcmtgfabnvo 65', 65, 15],
        ['sfkropatfwkna 95', 95, 59],
        ['kzibjralr 2', 2, 12],
        ['hnpmykspichx 34', 34, 87],
        ['armaholwvkttg 9', 9, 47],
        ['vswomwpuhpqzxstltlw 10', 10, 40],
    ]


    '''n = int(input())
    arr = [None] * n
    for i in range(n):
        in_data = list(input().split())
        arr[i] = in_data
        arr[i][0] = in_data[0]
        arr[i][1] = int(in_data[1])
        arr[i][2] = int(in_data[2])'''
    #arr = in_place_quick_sort(arr)
    in_place_quick_sort_index(arr, 0, len(arr) - 1)
    result = ''
    for elem in arr:
        result += elem[0] + '\n'
    print(result)
