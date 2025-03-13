#Prog06: Create a program that ask user to input 10 numbers. 
# Print the result of the first number minus all of the remaining numbers.

# Initialize a variable to store the input.
numbers = []
# Loop to ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
    numbers.append(num)
#     Subtract the first number to all of the remaining numbers.
    result = numbers[0] - sum(numbers[1:])
# Print the result.
print(result)