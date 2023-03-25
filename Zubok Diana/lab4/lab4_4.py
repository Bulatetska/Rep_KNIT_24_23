a = "a14b6fh"
unique = set(a)
result1 = len(unique) == len(a)
result2 = all(a.count(char) == 1 for char in a)
print("З використанням множини:", result1)
print("З використанням списку:", result2)