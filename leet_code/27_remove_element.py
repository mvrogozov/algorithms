def remove_element(nums: list, val: int) -> int:
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)


def main():
    nums = [3, 2, 2, 3]
    n = 3

    print(remove_element(nums, n))
    print(nums)

if __name__ == '__main__':
    main()
