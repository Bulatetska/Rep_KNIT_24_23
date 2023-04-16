lst = list()
n = int(input("Number of numbers in list: "))


if n == 0:
    print("List is empty")
else:
    for i in range(n):
        lst.append(int(input("Enter number: ")))
    
    def max_number(lst):
        max_val = max(lst)
        if max_val > 0:
            print("Max number of list is: ", max_val)
        elif max_val == 0:
            print("Max number of list is 0")
        else:
            return "Number is less than 0"
    
    max_number(lst)