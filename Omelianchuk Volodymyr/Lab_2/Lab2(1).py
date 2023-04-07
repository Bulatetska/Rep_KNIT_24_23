price = float(input("Повна вартість товару:"))

if price > 1000:
    price *= 0.9
elif price > 500:
    price *= 0.95
elif price > 100:
    price *= 0.97

print("Вартість з урахуванням знижки: {:.2f} грн".format(price))
