class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return -1

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')

    def get_stack(self):
        #print(self.items)
        return self.items


def is_correct_bracket_seq(input_data):
    OPEN_BRACKETS = ['(', '{', '[', -1]
    CLOSE_BRACKETS = [')', '}', ']']
    stack = Stack()
    for sign in input_data:
        if sign in OPEN_BRACKETS:
            stack.push(sign)
        elif CLOSE_BRACKETS.index(sign) != OPEN_BRACKETS.index(stack.pop()):
            print('False')
            return False
    print(not bool(stack.get_stack()))
    return not bool(stack.get_stack())


def main():
    input_data = input().strip()
    is_correct_bracket_seq(input_data)


#if __name__ == '__main__':
#    main()
main()
