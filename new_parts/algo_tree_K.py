import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left: 'Node'=None, right: 'Node'=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node: Node, l: int, r: int):
    if node.left and node.value >= l:
        print_range(node.left, l, r)
    if l <= node.value <= r:
        print(node.value)
    if node.right and node.value <= r:
        print_range(node.right, l, r)


# def print_range_less(node: Node, l: int, r: int):
#     if node.value >= l:
#         if node.left:
#             print_range_less(node.left, l, r)
#         else:
#             print(f'NO VAL LESS THAN {l}, value >= l and no left node -> {node.value}')
#         print(node.value)
#     else:
#         if node.right:
#             print_range_less(node.right, l, r)
#         else:
#             print((f'NO VAL GT l, value <= {l} and no right node -> {node.value}'))


# def print_range_great(node: Node, l: int, r: int):
#     if node.value <= r:
#         if node.right:
#             print_range_great(node.right, l, r)
#         else:
#             print(f'NO VAL GT {r}, value <= r and no right node -> {node.value}')
#         print(f'{node.value}')
#     else:
#         if node.left:
#             print_range_great(node.left, l, r)
#         else:
#             print((f'NO VAL LT r, value > {r} and no left node -> {node.value}'))


def test():
    node0 = Node(None, None, 3)
    node1 = Node(None, node0, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    l, r = 2, 8
    print(f'l={l}, r={r}')
    #print_range_less(node7, l, r)
    #print_range_great(node7, l, r)
    # expected output: 2 5 8 8
    print_range(node7, l, r)


if __name__ == '__main__':
    test()
