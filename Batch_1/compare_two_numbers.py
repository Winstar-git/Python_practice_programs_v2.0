# Prog01: Create a program that ask user to input 2 numbers.
# Print the bigger number.

# Ask the user to input the first number
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number
num2 = int(input("Enter the second number: "))
# Compare the two numbers
if num1 > num2:
    # If the first number is bigger, print it
    print(f"{num1} is bigger number")
else:
    # If the second number is bigger, print it
    print(f"{num2} is bigger number")