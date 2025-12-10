""""
 Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
"""
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
# perform addition
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print ("addition of " + str(num1) + " and " + str(num2) + " = " + str(addition))
print("subtraction of " + str(num1) + " and " + str(num2) + " = " + str(subtraction))
print("multiplication of " + str(num1) + " and " + str(num2) + " = " + str(multiplication))
print("division of " + str(num1) + " and " + str(num2) + " = " + str(division))

