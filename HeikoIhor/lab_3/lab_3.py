arr1 = list(range(1, 6))  # 1 2 3 4 5

# TASK 1
i = 0
while i < len(arr1):
    if arr1[i] % 2 == 0:
        del arr1[i]
    i += 1

print("TASK 1:")
print(arr1)

# TASK 2
arr1 = [i*i for i in arr1]

print("TASK 2:")
print(arr1)

# TASK 3

print("TASK 3:")
print(max(arr1))
