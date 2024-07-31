#This program will identify the program is odd or even
#Print welcome message
print("*** Welcome to Odd or Even Number finder *** \n")
# Get the number
number  = int(input("Enter the number: "))

result = number % 2

if (result != 0):
    print(f'The number {number} is Odd Number')
else:
    print(f'The number {number} is Even Number')

