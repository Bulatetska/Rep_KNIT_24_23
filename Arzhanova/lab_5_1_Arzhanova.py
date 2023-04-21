def max_int(list):
    maxInt= max(list)
    if maxInt > 0:
        return maxInt
    else:
        return "Число менше 0"

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_int(list))