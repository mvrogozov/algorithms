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


def get_sum_medians(amount: int, nums: list[int]):
    median_sum = 0
    cur_nums = []
    for num, val in enumerate(nums):
        cur_nums = insert_in_sorted(val, cur_nums) #sorted(nums[:num + 1])
        median_sum += cur_nums[num // 2]
    return median_sum


def main():
    a = 10
    nums = list(map(int, '5 10 8 1 7 3 9 6 2 4'.split()))
    print(get_sum_medians(a, nums))
    # a = []
    # res = insert_in_sorted(1, a)
    # print(res)


if __name__ == '__main__':
    main()
