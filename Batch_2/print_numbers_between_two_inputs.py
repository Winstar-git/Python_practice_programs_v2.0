#Prog10: Create a program that ask user to input 2 
# numbers. Print all the numbers between the two numbers.

# Ask the user to input the first number.
num1 = int(input("Enter the first number: "))
# Ask the user to input the second number.
num2 = int(input("Enter the second number: "))
#Loop from the smaller number to the larger number.
if num1 < num2:
    for i in range(num1 + 1,num2):
#     Print each number in the range.
        print(i, end="-")
else:
    for i in range(num2 + 1, num1):
            print(i, end="-")