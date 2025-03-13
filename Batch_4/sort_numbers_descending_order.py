#Prog04: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from highest to lowest. Clue: sort() function.
# 
# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input numbers until invalid input.
while True:
    try:
        num = int(input("Enter a number: "))
#     If successful, add the number to the list.
        numbers.append(num)
#     If input is invalid, break the loop.
    except ValueError:
        print("Invalid Input. Exitinng the program")
        break
# Sort the list of numbers in descending order.
descending_order = sorted(numbers, reverse=True)
# Display the sorted list of numbers.
print(f"Highest to Lowest: {descending_order}")