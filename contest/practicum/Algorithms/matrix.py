def read_input():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    x = int(input())
    y = int(input())
    return n,m,matrix,x,y

def neighbor(n,m,matrix,x,y):
    if (n == 1):
        if (m == 1):
            result = ''
        elif 0 < y < m -1:
            result = matrix[x][y-1], matrix[x][y+1]
        elif (y == 0) and (y < m-1):
            result = matrix[x][y+1]
        else:
            result =  matrix[x][y-1]
    elif 0 < x < n-1:
        if (m == 1):
            result = matrix[x-1][y], matrix[x+1][y]
        elif 0 < y < m-1:
            result = matrix[x-1][y], matrix[x+1][y], matrix[x][y-1], matrix[x][y+1]
        elif (y == 0) and (y < m-1):
            result = matrix[x-1][y], matrix[x+1][y], matrix[x][y+1]
        else:
            result = matrix[x-1][y], matrix[x+1][y], matrix[x][y-1]
    elif (x == 0) and (x < n-1):
        if (m == 1):
            result = matrix[x+1][y]
        elif 0 < y < m-1:
            result = matrix[x+1][y], matrix[x][y-1], matrix[x][y+1]
        elif (y == 0) and (y < m-1):
            result = matrix[x+1][y], matrix[x][y+1]
        else:
            result = matrix[x+1][y], matrix[x][y-1]
    
    else:
        if (m == 1):
            result = matrix[x-1][y]
        elif 0 < y < m-1:
            result = matrix[x-1][y], matrix[x][y-1], matrix[x][y+1]
        elif (y == 0) and (y < m-1):
            result = matrix[x-1][y], matrix[x][y+1]
        else:
            result = matrix[x-1][y], matrix[x][y-1]

    return result
'''
n,m,matrix,x,y = read_input()
result = neighbor(n,m,matrix,x,y)
if isinstance(result, int) or isinstance(result, str):
    print(result)
else:
    d = list(result)#.sort()
    d.sort()
    print(' '.join(map(str, d)))'''