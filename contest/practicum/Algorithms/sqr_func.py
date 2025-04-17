def read_input():
    a,x,b,c = list(map(int, input().strip().split()))
    return a,x,b,c

def sqr_func(a,x,b,c):
    return a*x*x+b*x+c

a,x,b,c = read_input()
print(sqr_func(a,x,b,c))