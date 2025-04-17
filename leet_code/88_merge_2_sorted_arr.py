num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
n = 3
m = 3
num1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
num2 = [1, 2, 2]

m = 0
num1 = [0]
num2 = [1]

num1 = [-1,-1,0,0,0,0]
m = 4
num2 = [-1, 0]

num1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 1
num2 = [-14,-11,-7,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]

# num1 = [1,0]
# m = 1
# num2 = [2]


# num1 = [-1,0,1,1,0,0,0,0,0]
# m = 4
# num2 = [-1,0,2,2,3]

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    pos1 = 0
    pos2 = 0
    if m == 0:
        nums1[0:] = nums2[0:]
        return
    while pos2 < len(nums2) and pos1 < len(nums1):
        if nums1[pos1] > nums2[pos2]:
            nums1[pos1 + 1:] = nums1[pos1:-1]
            nums1[pos1] = nums2[pos2]
            pos2 += 1
            pos1 += 1
            continue
        # if nums2[pos2] == 0 and nums1[pos1] == 0:
        #     pos2 += 1
        #     pos1 += 1
        #     continue
        if nums1[pos1] == 0 and pos1 >= m + pos2:
            nums1[pos1] = nums2[pos2]
            pos2 += 1
        pos1 += 1


def main():
    merge(num1, m, num2, n)
    print(num1)


if __name__ == '__main__':
    main()
