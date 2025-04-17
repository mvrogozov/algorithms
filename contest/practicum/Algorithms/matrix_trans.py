from random import random


def matrix_trans(rows, columns, matrix):
    result_matrix = [
        [matrix[i][j] for i in range(rows)] for j in range(columns)
    ]
    result = ''
    for i in range(columns):
        for j in range(rows):
            result += result_matrix[i][j] + ' '
        result += '\n'

    '''result_matrix = [[0] * rows for i in range(columns)]
    for i in range(columns):
        for j in range(rows):
            result_matrix[i][j] = matrix[j][i]'''
    return result

def matrix_trans2(rows, columns, matrix):
    result_matrix = [
        [matrix[i][j] for i in range(rows)] for j in range(columns)
    ]

    '''result_matrix = [[0] * rows for i in range(columns)]
    for i in range(columns):
        for j in range(rows):
            result_matrix[i][j] = matrix[j][i]'''
    return result_matrix



if __name__ == '__main__':
    rows = int(input())
    columns = int(input())
    #matrix = [input().split() for i in range(rows)]
    matrix = [
        [str(round(random() * j * 10, 2)) for j in range(columns)] for i in range(rows)]
    
    print(matrix_trans(rows, columns, matrix))
    #for i in range(columns):
    #    print(*matrix_trans2(rows, columns, matrix)[i])
