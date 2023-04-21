my_list = [4,3,2,1,3,2,5,1,5,3,1]
count = {}
for elem in my_list:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1
print(count)
