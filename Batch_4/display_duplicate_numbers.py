#Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
#   Append each number to the list.
    numbers.append(num)
# Initialize an empty list to store duplicate numbers.
duplicate_numbers = []
# Loop through the list of numbers.
for num in numbers:
#   If the number appears more than once in the list and is not already in the duplicate list, add it to the duplicate list.
    if numbers.count(num) > 1 and num not in duplicate_numbers:
        duplicate_numbers.append(num)
# Display the duplicate numbers.
print(f"The duplicate numbers  are: {duplicate_numbers}")