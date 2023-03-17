# -*- coding: utf-8 -*-

price = float(input("Введіть вартість товару: "))

if price > 1000:
    price *= 0.9
elif price > 500:
    price *= 0.95
elif price > 100:
    price *= 0.97

print("Вартість з урахуванням знижки: {:.2f} грн".format(price))

# # 2. Використання тернарного оператора для перевірки порожнього рядка
# input_str = input("Введіть рядок: ")
# result = input_str if input_str != "" else None

# print("Результат: ", result)