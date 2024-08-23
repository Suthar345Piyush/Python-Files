# factorial calculator
#problem: compute the factorial of a number using a while loop

number = 6
factorial = 1


while number > 0:
  #factorial = factorial * number
  #number = number - 1
   factorial *= number
   number -= 1


print("Factorial value of number is: " , factorial)