from heiko import squareNumbers, printResult
import mishchuk
import test

mishchuk.printMishchuk()
test.printTest()

numbers_arr = [1, 2, 3, 4, 5]
result_arr = []

squareNumbers(numbers_arr, result_arr)
printResult(result_arr)
