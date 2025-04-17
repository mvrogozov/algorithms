# 67918573


def max_score(
    hands: int,
    symbol_field,
    possible_values='123456789',
    hands_amount=2
) -> int:
    return sum(
        0 < symbol_field.count(digit) <= (hands * hands_amount)
        for digit in possible_values
        )


if __name__ == '__main__':
    print(max_score(
        hands=int(input()),
        symbol_field=f'{input()}{input()}{input()}{input()}')
    )
