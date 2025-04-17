# 68339495
class Dequeue:

    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__head = 0
        self.__tail = 0
        self.__max_size = max_size
        self.__size = 0

    def push_back(self, value):
        if self.__size >= self.__max_size:
            raise OverflowError('No more space in dequeue')
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, value):
        if self.__size >= self.__max_size:
            raise OverflowError('No more space in dequeue')
        self.__head = (self.__head - 1) % self.__max_size
        self.__queue[self.__head] = value
        self.__size += 1

    def pop_back(self):
        if self.__size == 0:
            raise Exception('Dequeue is empty')
        self.__tail = (self.__tail - 1) % self.__max_size
        result = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__size -= 1
        return result

    def pop_front(self):
        if self.__size == 0:
            raise Exception('Dequeue is empty')
        result = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return result

    def get_dequeue(self):
        return self.__queue


def main():

    command_amount = int(input())
    max_size = int(input())
    new_dequeue = Dequeue(max_size)
    for _ in range(command_amount):
        readed_command = input().strip().split()
        try:
            if (
                readed_command[0] == 'push_back' or
                readed_command[0] == 'push_front'
            ):
                new_dequeue.__getattribute__(
                    readed_command[0])(readed_command[1])
            if (
                readed_command[0] == 'pop_back' or
                readed_command[0] == 'pop_front'
            ):
                print(new_dequeue.__getattribute__(readed_command[0])())
        except Exception:
            print('error')


if __name__ == '__main__':
    main()
