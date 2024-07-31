
total = 0
#sum even numbers
for num in range(0,101):
    if num % 2 == 0:
        #print(num)
        total+=num
print(total)
total = 0
#sum even numbers
for num in range(2, 101, 2):
    total+=num
print(total)