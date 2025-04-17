def get_buy_day(day_number, arr, cost):
    if day_number >= len(arr):
        return -1
    if arr[day_number] >= cost:
        return day_number + 1
    return get_buy_day(day_number + 1, arr, cost)


def get_buy_day2(left, right, arr, cost):
    if left == right:
        if arr[left] >= cost:
            return left + 1
    mid = (right - left) // 2 + left
    if mid == left:
        if arr[mid] >= cost:
            return mid + 1
        mid = right
    if mid >= right:
        if arr[right] >= cost:
            return right + 1
        else:
            return -1
    if arr[mid] >= cost > arr[mid - 1]:
        return mid + 1
    if arr[mid] < cost <= arr[mid + 1]:
        return mid + 2
    if arr[mid] >= cost:
        right = mid
    else:
        left = mid
    return get_buy_day2(left, right, arr, cost)


def main():
    size = int(input())
    arr = list(map(int, input().split()))
    cost = int(input())
    print(get_buy_day2(0, size - 1, arr, cost), get_buy_day2(0, size - 1, arr, cost * 2))


if __name__ == '__main__':
    main()
