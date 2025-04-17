def best_deals(
    buyers_amount: int,
    sellers_amount: int,
    seller_prices: str,
    buyer_prices: str
) -> int:
    buyer_prices = sorted(list(map(int, buyer_prices.split())), reverse=True)
    seller_prices = sorted(list(map(int, seller_prices.split())))
    deals_amount = min(buyers_amount, sellers_amount)
    return sum(
        (buyer_prices[i] - seller_prices[i] for i in range(deals_amount) if (
            buyer_prices[i] - seller_prices[i] > 0
        )
        )
    )


def main():
    ba = 6
    sa = 5
    sp = '5 10 8 4 7 2'
    bp = '3 1 11 18 9'
    print(best_deals(ba, sa, sp, bp))


if __name__ == '__main__':
    main()
