# Set the counter to 0
count = 0

# Ask the user to input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))

    # Check if the number is odd
    if num % 2 != 0:
        count += 1

# Display the number of odd numbers
print("Total odd numbers:", count)