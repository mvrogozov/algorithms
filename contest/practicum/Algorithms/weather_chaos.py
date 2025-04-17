def read_input():
    n = int(input())
    t = list(map(int, input().strip().split()))
    return n,t

def w_chaos(n,t):
    days = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    t0 =t[0]
    t1 =t[1]
    if t[0] > t[1]:
        days = 1
    for i in range(1, n):
        if t[i-1] < t[i]:
            if i < n - 1:
                if t[i+1] < t[i]:
                    days += 1
            else:
                days += 1
    return days

if __name__ == '__main__':
    n,t = read_input()
    print(w_chaos(n,t))
