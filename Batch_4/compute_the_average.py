#Prog05: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the average.

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
# Calculate the average of the numbers in the list.
average = sum(numbers)/(len(numbers))
# Display the average.
print(f"The average number is: {average:.2f}")