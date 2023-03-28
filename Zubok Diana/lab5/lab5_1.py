def max_value(a):
    max_v = max(a);
    if max_v > 0:
        return max_v
    else:
        return "Число менше або дорівнює 0"
a = [-3, 0, 9, -7, 4]
print("Максимальне значення списку:", max_value(a))