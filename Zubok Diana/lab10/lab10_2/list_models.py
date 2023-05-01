import list_operations

lst = [5, 1, 0, -4, 4, 2, 6, -7, 0, 1]

sorted_lst =  list_operations.sort_list(lst)
print('Sorted:', sorted_lst)

l =  list_operations.find_element(lst, 2)
print('Element index:', l)

l =  list_operations.find_sequence(lst, [0,  -4, 4])
print('Index of the first element in the range:',l)

min_lst =  list_operations.find_min(lst, 5)
print('5 min_elements:', min_lst)

max_lst =  list_operations.find_max(lst, 5)
print('5 max_elements:', max_lst)

avg =  list_operations.average(lst)
print('Average:',avg)

unique_lst =  list_operations.remove_duplicates(lst)
print('List without duplicates:', unique_lst)