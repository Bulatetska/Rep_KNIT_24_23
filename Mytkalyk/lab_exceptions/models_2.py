from list_operations import *

lst = [5, 2, 8, 1, 9, 3, 5, 2, 8, 1]
sorted_lst = sort_list(lst)
print("Sorted list:", sorted_lst)

element = 9
found_element = find_element(lst, element)
print("Found element:", found_element)

sequence = [2, 8, 1]
sequence_found = find_sequence(lst, sequence)
print("Sequence found:", sequence_found)

first_min = find_first_min(lst)
print("First five minimum elements:", first_min)

first_max = find_first_max(lst)
print("First five maximum elements:", first_max)

average = calculate_average(lst)
print("Average:", average)

unique_lst = remove_duplicates(lst)
print("List with duplicates removed:", unique_lst)
