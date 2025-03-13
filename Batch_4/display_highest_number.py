#Prog03: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the highest number.

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
# Find and display the highest number in the list.
highest_number = max(numbers)
print(f"The highest number is: {highest_number}")