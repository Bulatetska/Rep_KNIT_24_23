
print("List A:")
A= [5, 4, 2, 1, 7, 8, 9, 10]
print(A)
print(" Task 1 :")
for i in A:
    if i % 2 == 0:
        A.remove(i)
       
print(A)
print("Task 2 :")
for i in range(len(A)):
    A[i] = A[i] ** 2

print(A)
print("Task 3 : ")
max_elem = max(A)

print(max_elem)