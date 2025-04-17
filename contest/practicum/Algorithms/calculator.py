# 68339503
import operator


class EmptyStackException(Exception):

    def __init__(self, message):
        self.message = message


class Stack:

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise EmptyStackException('Stack is empty')
        return self.__items.pop()


def calculator(input_data):
    stack = Stack()
    signs = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }
    for elem in input_data:
        operation = signs.get(elem)
        if not operation:
            stack.push(int(elem))
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.push(operation(operand_2, operand_1))
    return stack.pop()


def main():
    input_data = input().split()
    print(calculator(input_data))


if __name__ == '__main__':
    main()
