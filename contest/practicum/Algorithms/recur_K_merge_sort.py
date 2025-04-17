def merge_old(arr: list, left: int, mid: int, right: int) -> list:
    result = [None] * (right + 1)
    # print('incoming whole arr', arr)
    # print('borders = ', left, mid, right)
    # print('incoming = ', arr[left:mid], ' + ', arr[mid:right + 1])
    index_left = 0
    index_right = mid
    for index in range(right + 1):
        if index_left == mid:
            result[index:right + 1] = arr[index_right:right + 1]
            break
        if index_right == right + 1:
            result[index:right + 1] = arr[index_left:mid]
            break
        if arr[index_left] > arr[index_right]:
            result[index] = arr[index_right]
            index_right += 1
        else:
            result[index] = arr[index_left]
            index_left += 1
    return result


def merge_sort_old(arr: list, left: int, right: int) -> None:
    length = len(arr[left:right + 1])
    if length == 1:
        return [arr[left]]
    delta = length // 2
    # print('delta = ', right, left, delta)

    merge_sort(arr, left, right - delta)
    merge_sort(arr, right - delta + 1, right)

    '''if len(arr) == 1:
        return arr
    delta = len(arr) // 2

    m_left = merge_sort2(arr[0:delta], left, right - delta)
    m_right = merge_sort2(arr[delta:len(arr)], right - delta, right)'''

    #print('test', left, right, delta)
    #result = merge(arr[left:right], 0, delta, length - 1)
    if length % 2 != 0:
        delta += 1
    result = merge(arr[left:right + 1], 0, delta, length - 1)
    arr[left:right + 1] = result
    #print(result)
    return


def merge_sort_in_place(arr: list, left: int, right: int) -> None:
    if right - left == 1:
        return left
    delta = (right - left) // 2

    m_left = merge_sort(arr, left, right - delta)
    m_right = merge_sort(arr, right - delta, right)
    common_length = len(m_left) + len(m_right)
    print(f'm_right = {m_right}')
    if m_left and m_right:
        result = merge(arr, m_left, m_right, right - 1)[m_left:m_right + right - 1]
        print(result)
        return result

def merge_sort2(arr: list, left: int, right: int) -> None:
    if len(arr) == 1:
        return arr
    delta = len(arr) // 2

    m_left = merge_sort2(arr[0:delta], left, right - delta)
    m_right = merge_sort2(arr[delta:len(arr)], right - delta, right)
    
    #print(f'm_right = {m_right}')
    if m_left and m_right:
        common_length = len(m_left) + len(m_right)
        #result = merge(arr[left:right], left, len(m_left) , right - 1)
        #arr[left:right] = result
        result = merge(m_left + m_right, 0, len(m_left), common_length - 1)
        print(result)
        return result

# new try
# не проходит тест merge, merge_sort проходит

def merge(arr: list, left: int, mid: int, right: int):
    result = []
    if left == right:
        return [arr[left]]
    right_pointer = mid
    while left < mid and right_pointer < right:
        if arr[left] <= arr[right_pointer]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right_pointer])
            right_pointer += 1
    if left == mid:
        result.extend(arr[right_pointer:right])
    if right_pointer == right:
        result.extend(arr[left:mid])
    return result


def merge_sort(arr: list, left:int, right:int):
    if right - left <= 1: #  [3, 4)
        return
    if right - left == 2: #  [3, 4, 5)
        mid = left + 1
        arr[left:right] = merge(arr, left, mid, right)
        return
    mid = (right - left) // 2
    merge_sort(arr, left, left + mid)
    merge_sort(arr, left + mid, right)
    arr[left:right] = merge(arr, left, left + mid, right)

def main():
    command = input()
    n = int(input())
    arr = list(map(int, input().split()))
    if command == 'sort':
        merge_sort(arr, 0, n)
        print(*arr)
    else:
        print(merge(arr, 0, n, len(arr)))
    


def main1():
    arr = [1, 3, 5, 2, 4, 6, 7, 8, 9]
    left = 0
    mid = 3
    right = 9

    arr = [2, 1]
    left = 0
    mid = 1
    right = 2

    arr = [1]
    left = 0
    mid = 0
    right = 0

    arr = [4, 5, -9]
    left = 0
    mid = 1
    right = 3

    # arr = [9, 6, 4, 8, 3, 7, 5, 2, 1]
    # arr = [9, 6, 4, 8, 3, 7, 5, 2, 1, 3]
    # arr = [-19, -7]
    #arr = [17, 7]
    #arr = [3,2,5]
    #arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    #print(merge(arr, 0, 3, 5))
    print('arr= ', arr)
    #merge_sort(arr, 0, len(arr) - 1)
    #print(merge_sort2(arr, 0, 8))
    #merge_sort_in_place(arr, 0, 9)
    print(f'result = {merge(arr, left, mid, right)}')
    merge_sort(arr, left, len(arr))
    print(f'merge_sort result = {arr}')


if __name__ == '__main__':
    main1()

