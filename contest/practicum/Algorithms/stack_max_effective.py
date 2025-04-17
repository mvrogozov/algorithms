class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class Stack:

    def __init__(self):
        self.head = None
        self.max_item = None

    def push(self, item):
        if not self.head:
            self.head = Node(value=item)
            self.max_item = self.head
        else:
            new_node = Node(value=item, prev=self.head)
            self.head = new_node
            if item >= self.max_item.value:
                new_max_item = Node(value=item, prev=self.max_item)
                self.max_item = new_max_item

    def pop(self):
        if self.head:
            if self.head.value == self.max_item.value:
                self.max_item = self.max_item.prev
            self.head = self.head.prev
        else:
            print('error')

    def get_max(self):
        if self.head:
            print(self.max_item.value)
        else:
            print('None')

    def get_stack(self):
        print(self.items)

    def get_max_array(self):
        print(self.max_item)


def main():
    '''new_stack = Stack()
    new_stack.push(12)
    new_stack.push(15)
    new_stack.push(13)
    new_stack2 = Stack()

    print('result -> ', new_stack.items)
    print('pop = ', new_stack.pop())
    print(f'max = {new_stack.get_max()}')
    print(f'new_max= {new_stack2.get_max()}')
    print(f'new_pop = {new_stack2.pop()}')
'''
    stack = Stack()
    length = int(input())
    for index in range(length):
        readed_command = input().strip().split()
        if readed_command[0] == 'get_max':
            stack.get_max()
        if readed_command[0] == 'pop':
            stack.pop()
        if readed_command[0] == 'push':
            stack.push(int(readed_command[1]))
        if readed_command[0] == 'print':
            stack.get_stack()
        if readed_command[0] == 'max':
            stack.get_max_array()

        
        # print(readed_command)

#if __name__ == '__main__':
#    main()
main()
