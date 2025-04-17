def read_input():
    a = str(input())
    b = str(input())
    return a, b


def bin_sum(a, b):
    if len(a) < len(b):
        b, a = a, b
    dif = len(a) - len(b)
    b = '0' * dif + b
    c = ''
    buf = '0'
    for i in reversed(range(len(a))):
        if a[i] == b[i] == '0':
            if buf == '0':
                c = '0' + c
            else:
                c = '1' + c
                buf = '0'
        elif a[i] == b[i] == '1':
            if buf == '0':
                c = '0' + c
                buf = '1'
            else:
                c = '1' + c
        else:
            if buf == '0':
                c = '1' + c
            else:
                c = '0' + c
        if i == 0:
            if buf == '1':
                c = '1' + c
    return c

if __name__ == '__main__':
    a,b = read_input()
    print(bin_sum(a,b))