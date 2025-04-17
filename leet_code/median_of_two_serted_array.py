from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            average = (nums1[length // 2] + nums1[(length // 2) - 1]) / 2
        else:
            average = nums1[length // 2]
        #average = sum(nums1) / len(nums1)
        print(nums1)
        return average
    

def main():
    a = Solution()
    num1 = [1, 3]
    num2 = [2]
    print(a.findMedianSortedArrays(num1, num2))

if __name__ == '__main__':
    main()