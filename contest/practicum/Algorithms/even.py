def read_input():
    a,b,c = list(map(int, input().strip().split()))
    return a,b,c

def even_game(a,b,c):
    if a % 2 == 0:
        if b % 2 == 0:
            if c % 2 ==0:
                return 'WIN'
    elif b % 2 != 0:
        if c % 2 != 0:
            return 'WIN'
    return 'FAIL'

def odd_game(a,b,c):
# The same game
    if (
        (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
        ) or (
            (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0)
        ):
        return 'WIN'
    return 'FAIL'

a,b,c = read_input()

print(odd_game(a,b,c))