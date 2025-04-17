class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(node):
    if node.left:
        left = solution(node.left)
    else:
        left = node.value
    if node.right:
        right = solution(node.right)
    else:
        right = node.value
    return max(left, right, node.value)


def main():
    node = Node(11)
    node.value = 88
    left_node = Node(value=22)
    right_node = Node(value=33)
    node.left = left_node
    node.right = right_node
    left_node = Node(value=55)
    right_node.right = left_node
    print(solution(node))


if __name__ == '__main__':
    main()
