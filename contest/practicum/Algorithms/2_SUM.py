def read_input():
    l = int(input())
    n = list(map(int, input().strip().split()))
    k = int(input())
    return l,n,k

def caps(l,n,k):
    for i in range(l):
        for j in range(i+1,l):
            if (n[i] + n[j]) == k:
                return n[i], n[j]
    return None, None

l,n,k = read_input()
result = caps(l,n,k)
if result is None:
	print(None)
else:
	print(' '.join(map(str, result)))

#print(' '.join(map(str, caps(l,n,k))))