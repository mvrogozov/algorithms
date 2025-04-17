class Node:

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class QueueNode:

    def __init__(self):
        self.node = None
        self.head = None
        self.queue_size = 0

    def put(self, value):
        if self.node:
            new_node = Node(value, self.node)
            self.node.next = new_node
            self.node = new_node
        else:
            self.node = Node()
            self.head = self.node
            self.node.value = value
        self.queue_size += 1

    def get(self):
        if self.head:
            print(self.head.value)
            self.head = self.head.next
            if self.queue_size == 1:
                self.node = None
            self.queue_size -= 1
        else:
            print('error')

    def size(self):
        print(self.queue_size)

    def get_nodes(self):
        print(f'Size = {self.queue_size}')
        while self.node:
            print(self.node.value)
            self.node = self.node.prev


def main():
    command_amount = int(input())
    new_queue = QueueNode()
    for index in range(command_amount):
        readed_command = input().strip().split()
        if readed_command[0] == 'size':
            new_queue.size()
        if readed_command[0] == 'get':
            new_queue.get()
        if readed_command[0] == 'put':
            new_queue.put(int(readed_command[1]))


if __name__ == '__main__':
    main()
