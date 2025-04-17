def read_input():
    l = int(input())
    n = list(map(int, input().strip().split()))
    x = int(input())
    return l,n,x

def sum_mem(l,n,x):
    mem = set()
    for i in range(l):
        y = x - n[i]
        if y in mem:
            return y,n[i]
        else:
            mem.add(n[i])
    return None

l,n,k = read_input()
result = sum_mem(l,n,k)
if result is None:
    print(None)
else:
    print(' '.join(map(str, result)))