#Prog07: Create a program that ask user to input 10 numbers. 
#Print the sum of all the numbers.

# Initialize a variable to store the sum.
sum = 0
# Loop to ask the user to input 10 numbers.
for i in range(10):
#    Add each number to the sum.
    num = int(input(f"{i+1}. Enter a number: "))
    sum += num
# Print the sum.
print(f"The sum of all the numbers is: {sum}")