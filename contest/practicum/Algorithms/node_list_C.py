# Comment it before submitting
'''class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def node_print(node):
    while node:
        print(node.value)
        node = node.next_item
'''

def solution(node, idx):
    head = node
    if idx == 0:
        head = node.next_item
        return head
    while idx >= 1:
        previous_node = node
        node = node.next_item
        idx -= 1
    previous_node.next_item = node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # node_print(new_head)
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
