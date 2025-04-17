# 68691290
def broken_search(nums, target) -> int:
    right = len(nums) - 1
    left = 0
    while right >= left:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if (
                (nums[left] > target) and
                (nums[left] > nums[mid] > target)
            ) or (
                (nums[left] <= target) and
                (nums[left] > nums[mid] < target or nums[mid] > target)
                ):
            right = mid - 1
            continue
        if (
                (nums[left] > target) and
                (nums[left] <= nums[mid] > target or nums[mid] < target)
            ) or (
                (nums[left] <= target) and
                (nums[mid] < target)
                ):
            left = mid + 1
            continue
    return -1


if __name__ == '__main__':
    input()
    k = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, k))
