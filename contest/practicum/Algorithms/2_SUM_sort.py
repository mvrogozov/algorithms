def read_input():
    l = int(input())
    n = list(map(int, input().strip().split()))
    x = int(input())
    return l,n,x

def sum_sort(l,n,x):
    n.sort()
    left = 0
    right = len(n) - 1
    while left != right:
        if n[left] + n[right] == x:
            return n[left],n[right]
        if n[left] + n[right] > x:
            right -= 1
        else:
            left += 1
    return None

l,n,k = read_input()
result = sum_sort(l,n,k)
if result is None:
    print(None)
else:
    print(' '.join(map(str, result)))