def is_grade_4(num):
    i = 1
    while i <= num:
        if i == num:
            return True
        i *= 4
    return False

if __name__ == '__main__':
    num = int(input())
    print(is_grade_4(num))