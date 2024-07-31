#Enter the number to add the digits
inputvalue = input("Enter the input to add digits: ")
length = len(inputvalue)
total = 0
for i in range(length):
    total = total+int(inputvalue[i])
    print(f'Current total is {total} and input value of index {i} is{ inputvalue[i]}')

print(f'The total value is : {total}')

print(3 * 3 + 3 / 3 - 3)

