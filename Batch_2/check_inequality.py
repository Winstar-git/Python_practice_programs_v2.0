#Prog02: Create a program that ask user to input 2 numbers. 
# Print "Not Equal" when the numbers are not the same.

# Ask the user to input the first number.
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number.
num2 = int(input("Enter the second number: "))
# Compare the two numbers.
if num1 != num2:
# If the numbers are not the same, print "Not Equal".
    print(f"{num1} and {num2} are Not Equal")
# If the numbers are the same, print "Equal".
else:
    print(f"{num1} and {num2} are Equal")