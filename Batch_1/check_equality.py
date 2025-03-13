# Prog02: Create a program that ask user to input 2 numbers.
# Print "Equal" when the numbers are the same.

# Ask the user to input the first number
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number
num2 = int(input("Enter the second number: "))
# Compare the two numbers
if num1 == num2:
# Print "Equal" if the numbers are the same
    print(f"{num1} and {num2} are Equal")
# Print "Not Equal" if the numbers are not the same
else:
    print(f"{num1} and {num2} are Not Equal")