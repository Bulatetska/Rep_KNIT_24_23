price = float(input("Введіть вартість товару:"))

if price > 1000:
    discount = 0.1
elif price > 500:
    discount = 0.05
elif price > 100:
    discount = 0.03
else:
    discount = 0

total_price = price - (price * discount)

print("Ціна зі знижкою: ", total_price)