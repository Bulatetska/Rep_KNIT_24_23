def calculate_discounted_price(price):
    discount = 0
    if price > 1000:
        discount = 0.10
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03

    discounted_price = price - (price * discount)
    return discounted_price

# Приклад використання:
original_price = int(input("Введіть ціну: "))
final_price = calculate_discounted_price(original_price)
print("Вартість товару зі знижкою:", final_price)