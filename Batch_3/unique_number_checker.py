# Prog03: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

# Initialize an empty list to store the numbers.
numbers = []
# Loop to ask the user to input numbers until invalid input.
while True:
    try:
        num =input("Enter a number: ")
#       Try to convert the input to a number.
        num = int(num)
#       Check if the number is unique or duplicate and display the result.
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
#           Add to list for new input numbers
            numbers.append(num)            
#    If input is invalid, break the loop.
    except ValueError:
        print("Invalid Input. Exitinng the program")
        break