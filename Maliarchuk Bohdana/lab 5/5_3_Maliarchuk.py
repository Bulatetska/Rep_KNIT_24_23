number = int(input("Number: "))
power = int(input("Power: "))

def number_power(x, n):
    if n < 0:
        return print("Power must be greater than 0") 
    else:
        return print("Power of number is: ", x ** n)

number_power(number, power)