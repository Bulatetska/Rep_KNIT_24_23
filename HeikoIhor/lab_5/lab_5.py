# TASK 1
def comparison(myValue):
    if myValue > 0:
        return myValue
    else:
        return "Число менше ніж 0"


value = -5
print("(TASK 1) ", comparison(value))

# TASK 2
def lengthOfWord(myValue):
    count = 0
    for l in myValue:
        if l.isalpha():
            count = count + 1
    return count


value = "lab_6"
print("(TASK 2) ", lengthOfWord(value))


# TASK 3
def raiseNumber(myNumber, exponent):
    result = myNumber
    if exponent > 0:
        while exponent > 1:
            result = result * myNumber
            exponent = exponent - 1

    return result


value = 2
exponent = 5
print("(TASK 3) ", raiseNumber(value, exponent))

# TASK 4
def myRange(n):
    if n > 1:
        return list(range(1, n))


n = 10
print("(TASK 4) ", myRange(n))

# TASK 5
def areaRectangle(length, height):
    if (length > 0 and height > 0) and length != height:
        return length * height
    else:
        return "Invalid values entered "


length = 10
height = 5
print("(TASK 5) Area of rectangle", areaRectangle(length, height))