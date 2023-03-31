cost = float(input("Введіть вартість товару: "))

if cost > 1000:
    sale = 0.1
elif cost > 500:
    sale = 0.05
elif cost > 100:
    sale = 0.03
else:
    sale = 0

sale_cost = cost * sale
result = cost - sale_cost

print("Вартість товару зі знижкою:")
print(result)
