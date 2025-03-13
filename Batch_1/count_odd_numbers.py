#Prog08: Create a program that ask user to input 10 numbers. 
#Print how many are odd numbers.

# Initialize a counter for odd numbers.
count = 0 
# Loop to ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
#   Check if each number is odd.
    if num % 2 != 0:
#     Increment the counter if the number is odd.
         count += 1
# Print the counter.
print(f"There are {count} odd numbers.")