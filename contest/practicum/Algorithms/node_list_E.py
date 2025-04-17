# Comment it before submitting
'''class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev
'''

def solution(node):
    while node:
        node.prev, node.next = node.next, node.prev
        if node.prev is None:
            return node
        node = node.prev

'''def print_node(node):
    print(node.value)
    while node:
        print(f'node = {node.value}, next = {node.next}, prev = {node.prev} ')
        node = node.next
'''
def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1


if __name__ == '__main__':
    test()
