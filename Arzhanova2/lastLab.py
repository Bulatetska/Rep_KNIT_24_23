from lastLab_funk import *

my_list = [5, 2, 8, 1, 3, 5, 4, 2, 8, 7, 6]

sorted_list = sort_list(my_list)
print("Sorted List:", sorted_list)

element_index = find_element(my_list, 4)
print("Index of element 4:", element_index)

sequence_index = find_sequence(my_list, [2, 8])
print("Index of sequence [2, 8]:", sequence_index)

first_min_elements = find_first_min_elements(my_list, 5)
print("First 5 minimum elements:", first_min_elements)

first_max_elements = find_first_max_elements(my_list, 5)
print("First 5 maximum elements:", first_max_elements)

average = calculate_average(my_list)
print("Average:", average)

unique_list = remove_duplicates(my_list)
print("Unique List:", unique_list)

empty_list = []
average = calculate_average(empty_list)

#my_list_error = [5, 2, '8', 1, 3, 5, 4, 2, 8, 7, 6]
#sorted_list = sort_list(my_list_error)