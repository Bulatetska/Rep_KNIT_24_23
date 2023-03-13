print("Завдання №1 ")
price = float(input("Введіть вартість товару: "))

if price > 1000:
    discount = 0.1
elif price > 500:
    discount = 0.05
elif price > 100:
    discount = 0.03
else:
    discount = 0

disamount = price * discount
result = price - disamount
print("Знижка: {:.0%}".format(discount))
print("Вартість товару зі знижкою: {:.2f} грн".format(result))

print("Завдання №2 ")
value = input("Введіть рядкове значення: ")

result = value if value != "" else None

print(result)
