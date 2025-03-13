#Prog04: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers without the decimal point.

# Ask the user to input the first number.
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number.
num2 = int(input("Enter the second number: "))
# Calculate the quotient of the two numbers.
# Print the quotient without the decimal point.
print(f"The quotient of the two numbers is: {num1/num2:.0f}" )