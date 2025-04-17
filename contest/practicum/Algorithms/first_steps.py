def read_input():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


def zipper(a, b):
    length = len(a)
    c = [(a[i], b[i]) for i in range(length)]
    result = []
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    return result


def zipper2(a, b):
    c = zip(a,b)
    print(*c)


def main():

    #a, b = read_input()
    a = ['a', 'c', 'e', 'g']
    b = ['b', 'd', 'f', 'h']
    c = ['1']
    c *= 4
    print(c.__iter__())
    zipper2(a, b)
    print('zipper = ', *zipper(a, b))
    print(' '.join(map(str, zipper(a, b))))

if __name__=='__main__':
    main()
