# first code in python
number1 = float(input("enter number-1"))
number2 = float(input("enter number-2"))
operator = input("enter an operator")

# Check the operator and perform the corresponding operation
if operator == "+":
 output = number1 + number2

if operator == "-":
 output = number1 - number2

if operator == "*":
 output = number1 * number2

if operator == "/":
 output = number1 / number2

# Display the result of the calculation
print("Your calculation is: ", output)
