price = float(input("Введіть вартість товару: "))

if price > 1000:
    discount = 0.1
elif price > 500:
    discount = 0.05
elif price > 100:
    discount = 0.03
else:
    discount = 0

discount_amount = price * discount
total_price = price - discount_amount

print("Вартість зі знижкою: ", total_price)
