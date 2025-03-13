# Prog02: Create a program that asks the user to input numbers,
# continuing until the user input is invalid.
# Display the number with the most duplicates.

# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input numbers until invalid input.
while True:
    try:
#     Try to convert the input to a number.
        num = int(input("Enter a Number: "))
#           if successful, add the number to the list.
        numbers.append(num)
#     If input is invalid, break the loop.
    except ValueError:
        print("Invalid Input. Exitinng the program")
        break
# Initialize a variable to track the most frequent number and its count.
most_frequent = None
highest_count = 0
count = 0
# Loop through the list of numbers.
for num in numbers:
#    Count the occurrences of each number.
    count = numbers.count(num)
#     If the count is higher than the current highest count, update the most frequent number.
    if count > highest_count:
        highest_count = count
        most_frequent = num
# Display the number with the most duplicates.
print(f"The number with the most duplicates is: {most_frequent} (appeared {highest_count} times)")
