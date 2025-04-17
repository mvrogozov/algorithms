def merge_beds(arr):
    arr.sort()
    length = len(arr)
    result = []
    index = 0
    while index < length:  # if index==len ???
        if index == length - 1:
            result.append(arr[index])
            break
        if arr[index][1] >= arr[index + 1][0]:
            left = arr[index][0]
            right = max(arr[index + 1][1], arr[index][1])
            while index < length - 1 and right >= arr[index + 1][0]:
                right = max(arr[index][1], arr[index + 1][1], right)
                index += 1
                
            result.append([left, right])
        else:
            result.append(arr[index])
        index += 1
    for elem in result:
        print(*elem)
    #print(arr)
    #print(result)


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, (input().split()))))
    merge_beds(arr)

def main1():
    #arr = [[2, 3], [1, 2], [4, 8], [5, 10], [11, 12], [13, 14]]
    arr = [[7, 8], [7, 8], [2, 3], [6, 10]]
    arr = [[19, 68], [48, 56], [59, 96], [1, 5], [17, 58], [2, 24]]
    merge_beds(arr)


if __name__ == '__main__':
    main()
