# Set the total to 0
total = 0

# Ask the user to input 10 numbers
for i in range(10):
    num = float(input("Enter a number: "))

    # Add the number to the total
    total += num

# Display the total sum
print("The total sum is:", total)