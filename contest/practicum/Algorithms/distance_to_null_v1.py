'''def find_distance1(n, l):
    distance_list = []
    for i in range(n):
        to_left = 0
        to_right = 0
        for j in range(0, n):
            if l[i - to_left] == '0':
                distance_list.append(str(to_left))
                break
            if l[i + to_right] == '0':
                distance_list.append(str(to_right))
                break
            if to_left < i:
                to_left += 1
            if i + to_right < n - 1:
                to_right += 1
    return distance_list
'''
# 67883003
from typing import Tuple, List


def read_input() -> Tuple[int, List[str]]:
    n: int = int(input())
    house_list: List[str] = list(input().strip().split())
    return n, house_list


def find_distance(n: int, l: list) -> List[str]:
    distance_list: List = []
    null_indexes: List = []
    j: int = 0
    null_count: int = l.count('0')
    for i in range(null_count):
        null_indexes.append(l.index('0', j))
        j = null_indexes[-1] + 1
    for i in range(n):
        to_left: int = abs(i - null_indexes[j])
        to_right: int = to_left
        if j < null_count - 1:
            to_right = abs(null_indexes[j+1] - i)

        if to_left <= to_right:
            distance_list.append(to_left)
        else:
            distance_list.append(to_right)
            if j < null_count - 1:
                j += 1
    return distance_list


if __name__ == '__main__':
    n, house_list = read_input()
    print(' '.join(map(str, find_distance(n, house_list))))
