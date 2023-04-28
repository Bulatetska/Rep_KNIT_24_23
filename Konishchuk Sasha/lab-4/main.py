# Task 1
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

print("Elements of A that are not in B:")
print(A - B)

# Task 2
print("\nCommon elements of A and B:")
print(A & B)

# Task 3
print("\nUnion of sets A and B:")
print(A | B)

# Task 4
a = "a14b6fh"
if len(set(a)) == len(a):
    print("\nAll characters are unique")
else:
    print("\nThere are repeating characters")

# Task 5
lst = [3, 5, 11, 7, 4, 3, 11, 10, 3]
my_dict = {}
for i in lst:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print("\nFrequency count of elements in list:")
print(my_dict)

# Task 6
my_dict = {2: "apple", 5: "banana", 1: "orange", 4: "pear"}

print("\nValues with even keys:")
for key in my_dict:
    if key % 2 == 0:
        print(my_dict[key])

# Task 7
my_dict = {"apple": 3, "banana": 5, "orange": 2, "pear": 4}

to_delete = []
for key in my_dict:
    if key.startswith("a"):
        to_delete.append(key)

for key in to_delete:
    del my_dict[key]

print(my_dict)

