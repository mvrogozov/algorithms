def read_data(n: int, data: str, k):
    result = list(map(int, data.split(' ')))
    #result = (int(val) for val in data.split(' '))
    return result, int(k)


def find_k_dif1(data: list, k):
    data.sort()
    dif = []
    for index in range(len(data) - 1):
        dif.append(data[index + 1] - data[index])
    dif.append(data[-1] - data[0])
    dif.sort()
    print(dif)
    return dif[k - 1]


def insert_in_sorted(num: int, nums: list):
    length = len(nums)
    left = nums[:length // 2]
    right = nums[length // 2:]
    if not left:
        if not right:
            return [num]
        if num > right[0]:
            right.append(num)
        else:
            right.insert(0, num)
        return right

    if num > left[-1]:
        result = left + insert_in_sorted(num, right)
    else:
        result = insert_in_sorted(num, left) + right
    return result

def find_k_dif(data: list, k):
    data.sort()
    dif = []
    length = len(data)
    #print(data)
    for i in range(length - 1):
        # for j in range(i + 1, length):
        for j in range(i + 1, length):
            cur_dif = abs(data[j] - data[i])
            if len(dif) < k:
                #dif.append(cur_dif)
                dif = insert_in_sorted(cur_dif, dif)
            else:
                # current_max_difs = max(dif)
                # if current_max_difs < cur_dif:
                #     break
                # max_index = dif.index(current_max_difs)
                # dif[max_index] = min(dif[max_index], cur_dif)
                if dif[-1] < cur_dif:
                    break
                dif = insert_in_sorted(cur_dif, dif)[:-1]
                # dif.append(cur_dif)
                # dif.sort()
                # dif.pop()
    #dif.sort()        
    #print(dif)
    return dif[k - 1]


def main():
    #data, k = read_data(input(), input(), input())
    data, k = read_data(3, '7 2 7 3', 4)
    data, k = read_data(3, '3 1 3 1 1', 1)
    data, k = read_data(3, '2 3 4', 2)

    print(find_k_dif(data, k))


if __name__ == '__main__':
    main()
