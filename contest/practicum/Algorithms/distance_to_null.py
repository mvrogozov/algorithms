# 67917777
from typing import List


def get_distances_to_null(
    nums,
    looking_for='0'
) -> List[int]:
    nums_length = len(nums)
    distances: List[int] = [0] * nums_length
    zeros = [index for index, value in enumerate(nums) if value == looking_for]
    zeros_start, zeros_end = zeros[0], zeros[-1]
    distances[:zeros_start] = [
        zeros_start - index for index in range(zeros_start)
    ]
    #for index in range(0, zeros_start):
    #    distances[index] = zeros_start - index
    for start, stop in zip(zeros, zeros[1:]):
    #for zeros_index in range(len(zeros) - 1):
    #    start = zeros[zeros_index]
    #    stop = zeros[zeros_index + 1]
        for index in range(start + 1, stop):
            distances[index] = min(index - start, stop - index)
    for index in range(zeros_end + 1, nums_length):
        distances[index] = index - zeros_end
    return distances


if __name__ == '__main__':
    input()
    print(*get_distances_to_null(input().split()))
