
#TASK 1
print("TASK_1:")
numbers = [9,6,2,4,9,6,2,1,0,3] 
print("Original List:", numbers)

del numbers[1::2]

print("List after deleting even elements:", numbers)

#TASK 2
print("\nTASK_2:")
list1 = list(range(1,10)) #create list of numbers from 1 to 10
list1 = [i*i for i in list1]

print("List after squaring:", list1)

#TASK 3
print("\nTASK_3:")
list2 = list(range(10,20)) #create list of numbers from 1 to 10
print(list2)

maxElement = max(list2)
print("Max Element:", maxElement)

