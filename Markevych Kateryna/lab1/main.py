price = float(input("Input price: "))
if price > 100 and price <= 500:
    discount = 0.03
elif price>500 and price<=1000:
    discount=0.05
elif price>1000:
    discount=0.1
else:
    discount = 0
new_price=price-(price*discount)
print(("New price:"),new_price)
