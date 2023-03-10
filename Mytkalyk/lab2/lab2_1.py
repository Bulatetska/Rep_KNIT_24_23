def calculate_price(price):
    if price > 1000:
        discount = 0.1
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03
    else:
        discount = 0
    discounted_price = price * (1 - discount)
    return discounted_price

print(calculate_price(50))
print(calculate_price(150))
print(calculate_price(550))
print(calculate_price(1050))