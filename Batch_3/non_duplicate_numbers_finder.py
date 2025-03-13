# Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that don't have duplicate.

# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
#     Append each number to the list.
    numbers.append(num)
# Initialize an empty list to store unique numbers.
unique_numbers = []
# Loop through the list of numbers.
for num in numbers:
#     If the number appears only once in the list, add it to the unique numbers list.
    if numbers.count(num) == 1:
        unique.append(num)
# Display the unique numbers.
print(f"List of numbers: {unique}")