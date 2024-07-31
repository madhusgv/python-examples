#This program will calculate the bill , tip for each person should pay
print("\n***Welcome to the tip calculator***\n")
#Get the total bill
total_bill = float(input("Enter the total bill: $"))
#Tip percentage
tip_percentage = int(input("Enter the tip percentage: "))
#Sharing
sharing_persons = int(input("How many persons are sharing? "))

sharing_amount = (total_bill+((total_bill*(tip_percentage/100))))/sharing_persons
final_amount = "{:.2f}".format(sharing_amount)

print(f'Each person should pay : ${final_amount}')