#Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

#Compare the numbers
if number1 > number2:
    print("The bigger number is:", number1)
elif number2 > number1:
    print("The bigger number is:", number2)
else:
    print("Both numbers are equal")