# Вартість товару без знижки
price = 1200

# Визначення величини знижки
if price > 1000:
    discount = 0.1
elif price > 500:
    discount = 0.05
elif price > 100:
    discount = 0.03
else:
    discount = 0

# Розрахунок вартості товару з урахуванням знижки
final_price = price * (1 - discount)

print("Кінцева вартість товару з урахуванням знижки: ", final_price)