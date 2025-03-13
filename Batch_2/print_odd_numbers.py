#Prog08: Create a program that print all the odd numbers 
# starting from 0 to 100. (Use while loop)

# Initialize a variable to 0.
num = 0 
# Loop while the variable is less than or equal to 100.
while num <= 100:
#     Check if the variable is odd.
    if num % 2 != 0:
#     If the variable is odd, print it.
        print(num, end="-")
#     Increment the variable by 1.
    num += 1