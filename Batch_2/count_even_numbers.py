#Prog07: Create a program that ask user to input 10 numbers. 
# Print how many are even numbers.

# Initialize a counter for even numbers.
even = 0
# Loop to ask the user to input 10 numbers.
for i in range(10):
#     Check if each number is even.
    num = int(input(f"{i+1}. Enter a number: "))
    if num % 2 == 0:
#     Increment the counter if the number is even.
        even += 1
# Print the counter.
print(f"There are {even} even numbers")