from typing import List


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def lmr_tree(root, result=[]):
    if root.left:
        result = lmr_tree(root.left)
    result += [root.value]
    if root.right:
        result = lmr_tree(root.right)
    return result


def solution(root: Node) -> bool:
    tree: List = lmr_tree(root)
    for index in range(len(tree) - 1):
        if tree[index] >= tree[index + 1]:
            return False
    return True


def main():
    n1 = Node(1)
    n2 = Node(7)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n8 = Node(8)
    n5.left = n3
    n5.right = n8
    n3.left = n1
    n3.right = n4
    n1.right = n2
    #print(is_find_tree(n5))
    #print(lmr_tree(n5))
    #print(solution(n5))
    #print(solution(n5))
    print(lmr_tree(n5))
    print(lmr_tree(n3))


if __name__ == '__main__':
    main()
