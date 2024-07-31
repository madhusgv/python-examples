# This program calculates body mass index(BMI)

#Get the height in Centimeter
height = input("Enter your height in centimeter: ")
#Get the weight in kilograms
weight = input("Enter your weight in kilograms: ")

heightinmeter = int(height)/100
bmi = int(weight)/(heightinmeter**2)

print(f'Your BMI is : {int(bmi)}')

