def calc(data: list[str]):
    stack = []
    for val in data:
        if val == '+':
            res = int(stack.pop()) + int(stack.pop())
            stack.append(res)
        elif val == '*':
            res = int(stack.pop()) * int(stack.pop())
            stack.append(res)
        elif val == '-':
            res = 0 - int(stack.pop()) + int(stack.pop())
            stack.append(res)
        elif val == '/':
            res = 1 / int(stack.pop()) * int(stack.pop())
            stack.append(res)
        else:
            stack.append(val)
    return int(stack.pop())

data = list(input().strip().split())
print(calc(data))

print(data)

data = ['8', '9', '+', '1', '7', '-', '*']
print(calc(data))

data = ['8', '9', '+', '1', '7', '-', '*', '102', '/']
print(calc(data))
