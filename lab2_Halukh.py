

def calculate_price():
    price = float(input("Введіть ціну товару: "))
    if price > 1000:
        discount = 0.1
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03
    else:
        discount = 0
    discounted_price = price * (1 - discount)
    print("Ціна зі знижкою:", discounted_price)


calculate_price()
