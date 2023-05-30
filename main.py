from heiko import squareNumbers, printResult
import mishchuk
import test

print(mishchuk.add(1, 2))
test.printTest()

numbers_arr = [1, 2, 3, 4, 5]
result_arr = []

squareNumbers(numbers_arr, result_arr)
printResult(result_arr)
