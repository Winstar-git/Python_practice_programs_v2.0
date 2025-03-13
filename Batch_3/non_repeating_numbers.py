#Prog02: Create a program that ask user to input 10 numbers. 
# Display all numbers. For numbers with duplicate, display only the first entry.

# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
#     Append each number to the list.
    numbers.append(num)
# Initialize an empty list to store numbers to be displayed.
display_numbers = []
# Loop through the list of numbers.
for num in numbers:
#     If the number is not already in the display list, add it.
    if num not in display_numbers:
        display_numbers.append(num)
# Display the numbers.
print(f"List of numbers (first occurrences only): {display_numbers}")