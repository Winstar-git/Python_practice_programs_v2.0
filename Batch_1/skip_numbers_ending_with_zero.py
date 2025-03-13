#Prog10: Create a program that print all the 
#numbers starting from 0 to 100 except numbers ending in zero.

# Loop from 0 to 100.
for i in range(1, 101):
#     Check if the current number does not end in zero.
    if i % 10 !=0:
#     If the number does not end in zero, print it.
        print(i, end="-")