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
    ans = stack.pop()
    if stack:
        raise ValueError
    return int(ans)


def parse_string(data: str):
    ops = ['(', ')', '-', '+', '*', ' ']
    res = []
    operand = ''
    for sign in data:
        if sign.isdigit():
            operand += sign
        elif sign in ops:
            if operand:
                res.append(operand)
                operand = ''
            # ?
            if sign != ' ':
                res.append(sign)
        else:
            return None
    if operand:
        res.append(operand)
    return res


def to_postfix(data: list):
    ans = []
    stack = []
    if not data:
        return None
    for item in data:
        if item.isalnum():
            ans.append(item)
            continue
        if item == '*':
            while stack and stack[-1] == '*':
                ans.append(stack.pop())
            stack.append(item)
            continue
        if item in ('+', '-'):
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(item)
            continue
        if item == '(':
            stack.append(item)
            continue
        if item == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return None
            continue
    ans.extend(stack[::-1])
    return ans


def parse_and_calc(data: str):
    data = parse_string(data)
    if not data:
        return 'WRONG'
    postfix = to_postfix(data)
    try:
        ans = calc(postfix)
    except Exception:
        return 'WRONG'
    return ans


data = input()
print(parse_and_calc(data))


data = '1+(2*2 - 3)'
print(data)
print(parse_and_calc(data))
print()
# 2

data = '+2+1'
print(data)
print(parse_and_calc(data))
print()
# WRONG

data = '1+2+1'
print(data)
print(parse_and_calc(data))
print()
# WRONG

data = '1++1'
print(data)
print(parse_and_calc(data))
print()
# WRONG

data = '1+a+1'
print(data)
print(parse_and_calc(data))
print()
# WRONG

data = '1 1 + 2'
print(data)
print(parse_and_calc(data))
print()
# WRONG

data = '11 + 2'
print(data)
print(parse_and_calc(data))
print()
# 13