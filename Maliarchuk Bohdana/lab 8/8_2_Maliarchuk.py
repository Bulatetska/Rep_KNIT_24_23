import sort_list
import find_element
import find_elements
import first_five_min
import first_five_max
import find_avg
import return_list

lst = []
n = int(input("number of elements in list: "))
for i in range(n):
    lst.append(int(input("enter element: ")))

element = int(input("which element to find: "))

sequence = []
num = int(input("number of elements in sequence: "))
for i in range(num):
    sequence.append(int(input("enter element: ")))

sort_list.sort_list(lst)
find_element.find_element(lst, element)
find_elements.find_sequence(lst, sequence)
first_five_min.find_first_five_min(lst)
first_five_max.find_first_five_max(lst)
find_avg.average(lst)
return_list.remove_duplicates(lst)
