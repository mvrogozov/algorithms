def read_input():
    n = int(input())
    x = list(input().strip().split())
    k = int(input())
    return n,x,k

def sum_list(n,x,k):
    num_s = ''
    for i in range(n):
        num_s += str(x[i])
    sum_d = int(num_s) + k
    sum_list = []
    while sum_d > 0:
        sum_list.append(sum_d % 10)
        sum_d = sum_d // 10
    sum_list.reverse()
    return sum_list

if __name__ == '__main__':
    n,x,k = read_input()
    print(' '.join(map(str, sum_list(n,x,k))))