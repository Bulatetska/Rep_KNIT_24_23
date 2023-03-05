DISCOUNT = (
    (1000, 0.1),
    (500, 0.05),
    (100, 0.03),
)


def get_discount(price: float) -> float:
    for limit, discount in DISCOUNT:
        if price > limit:
            return discount


if __name__ == "__main__":
    price = float(input("Введіть вартість товару: "))
    discount = get_discount(price)
    price_discounted = price - price * discount
    print(price_discounted)
