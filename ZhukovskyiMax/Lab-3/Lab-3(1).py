print("List Main:")
Main = [5, 4, 2, 1, 7, 8, 9, 10]
print(Main)
print(" Task 1 :")
for i in Main:
    if i % 2 == 0:
        Main.remove(i)

print(Main)
print("Task 2 :")
for i in range(len(Main)):
    Main[i] = Main[i] ** 2

print(Main)
print("Task 3 : ")
max_elem = max(Main)

print(max_elem)