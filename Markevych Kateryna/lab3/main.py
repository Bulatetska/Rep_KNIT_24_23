list = [1,2,3,4,5,6,67,7,8,9,10]
for i in list:
    if i % 2 == 0:
        list.remove(i)
print(list)
list = [i ** 2 for i in list]
print(list)
max_element = max(list)
print(max_element)