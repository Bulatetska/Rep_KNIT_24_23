price = float(input("Enter price: "))

def serchSell(price):
    if price > 1000:
        pricediscount = 0.1
    elif price > 500:
        pricediscount = 0.05
    elif price > 100:
        pricediscount = 0.03
    else:
        pricediscount = 0

    sum = price * pricediscount
    allPrice = price - sum
    print(f"discount: {allPrice:.2f} $")


serchSell(price)