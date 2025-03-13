# Prog01: Create a program that ask user to input 2 numbers. 
# Print the smaller number.

# Ask the user to input the first number.
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number.
num2 = int(input("Enter the second number: "))
if num1 < num2:
# Compare the two numbers. Print the smaller number.
    print(f"{num1} is smaller number.")
else:
    print(f"{num2} is smaller number.")
