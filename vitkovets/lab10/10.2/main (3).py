
import printing_functions

lst = [0, 8, 4, 8, 3, 7, 3, 2, 6, 7]

sorted_lst =  printing_functions.sort_list(lst)
print(sorted_lst)
index =  printing_functions.find_element(lst, 5)
print(index)

index =  printing_functions.find_sequence(lst, [4,  8, 3])
print(index)

min_lst =  printing_functions.find_min(lst, 5)
print(min_lst)

max_lst =  printing_functions.find_max(lst, 5)
print(max_lst)

avg =  printing_functions.average(lst)
print(avg)

unique_lst =  printing_functions.remove_duplicates(lst)
print(unique_lst)