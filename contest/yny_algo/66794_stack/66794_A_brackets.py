def is_psp(data: str):
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    stack = []
    for item in data:
        if item in opened:
            stack.append(item)
        if item in closed:
            if not stack:
                return 'no'
            prev = stack.pop()
            if closed.index(item) != opened.index(prev):
                return 'no'
    return 'no' if stack else 'yes'

data = input()
print(is_psp(data))

data = '('
print(is_psp(data))

data = '()[]{)'
print(is_psp(data))



#data = input()