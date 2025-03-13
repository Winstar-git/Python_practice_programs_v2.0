#Prog09: Create a program that print all the numbers 
# starting from 0 to 100 except numbers ending in zero or ending five.

# Loop from 0 to 100
for i in range(0, 101):
    # Check if the number is NOT a multiple of 5
    if i % 5 != 0:
        # Print the number on the same line
        print(i, end="-")