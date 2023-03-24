price = float(input("Введіть вартість товару: "))

if price >= 1000:
    discount = 0.1
elif price >= 500:
    discount = 0.05
elif price >= 100:
    discount = 0.03
else:
    discount = 0

discount_suma = price * discount
price_with_discount = price - discount_suma

print(f"Вартість зі знижкою: {price_with_discount} грн")

string = input("Введіть рядкове значення: ")
result = string if string != "" else None
print(result)