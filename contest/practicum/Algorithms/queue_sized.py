class MyQueueSized():

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, value):
        if self.count >= self.max_size:
            print('error')
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.count += 1

    def peek(self):
        print(self.queue[self.head])

    def pop(self):
        print(self.queue[self.head])
        self.queue[self.head] = None
        if self.count > 0:
            self.head = (self.head + 1) % self.max_size
            self.count -= 1

    def size(self):
        print(self.count)


def main():
    command_amount = int(input())
    max_size = int(input())
    new_queue = MyQueueSized(max_size)
    for index in range(command_amount):
        readed_command = input().strip().split()
        if readed_command[0] == 'size':
            new_queue.size()
        if readed_command[0] == 'pop':
            new_queue.pop()
        if readed_command[0] == 'push':
            new_queue.push(int(readed_command[1]))
        if readed_command[0] == 'peek':
            new_queue.peek()


if __name__ == '__main__':
    main()
