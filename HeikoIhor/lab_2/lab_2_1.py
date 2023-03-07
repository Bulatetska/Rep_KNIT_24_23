
cost = 600

if cost > 100 and cost < 500:
    finalCost = cost - (cost * 0.03)
elif cost > 500 and cost < 1000:
    finalCost = cost - (cost * 0.05)
elif cost > 1000:
    finalCost = cost - (cost * 0.1)
else:
    finalCost = 0

print("Cost:", finalCost)
