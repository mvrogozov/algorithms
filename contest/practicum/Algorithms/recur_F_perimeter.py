def get_max_perimeter(n: int, sides: list) -> int:
    sides.sort(reverse=True)
    a, b, c = sides[:3]
    for num in range(3, len(sides) + 1):
        if a < (b + c):
            return sum((a, b, c))
        a, b, c = b, c, sides[num]


def main():
    n = input()
    s = list(map(int, input().split()))
    print(get_max_perimeter(n, s))


if __name__ == '__main__':
    main()

# 6 3 3 2