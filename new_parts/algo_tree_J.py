import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if not LOCAL:
    from node import Node

if LOCAL:
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root: Node, key: int) -> Node:
    if root.value > key:
        if root.left:
            insert(root.left, key)
        else:
            root.left = Node(value=key)
    else:
        if root.right:
            insert(root.right, key)
        else:
            root.right = Node(value=key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()