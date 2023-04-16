height = int(input("Input height: "))
length = int(input("Input lenght: "))

def calculate_area(h, l):
    if h <=0 or l <= 0:
        print("Error")
    else:  
        area = h * l
        return print("Area is: ", area)

calculate_area(height, length)