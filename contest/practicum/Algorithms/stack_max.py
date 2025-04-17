class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')

    def get_stack(self):
        print(self.items)


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
        
        # print(readed_command)

#if __name__ == '__main__':
#    main()
main()
