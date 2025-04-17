def get_min_psp(n: int, w: str, s: str):
    stack = []
    weight = {w[i]: i for i in range(len(w))}
    opened = ['(', '[']
    closed = [')', ']']
    free_space = n - len(s)
    ans = ''
    for sign in s:
        if sign in opened:
            stack.append(sign)
        else:
            stack.pop()
    while len(ans) < free_space: 
        if len(stack) + len(ans) == free_space:
            ans += closed[opened.index(stack.pop())]
            continue
        for sign, pos in weight.items():
            if sign in closed:
                if stack and closed[opened.index(stack[-1])] == sign:
                    stack.pop()
                    ans += sign
                    break
            if sign in opened:
                ans += sign
                stack.append(sign)
                break
    return s + ans


n = int(input())
w = input()
s = input()
print(get_min_psp(n, w, s))

n = 6
w = '][)('
s = '(['
print(get_min_psp(n, w, s))
print()

n = 6
w = '()[]'
s = '([()'
print(get_min_psp(n, w, s))
print()

n = 4
w = '][)('
s = '()[]'
print(get_min_psp(n, w, s))
print()

