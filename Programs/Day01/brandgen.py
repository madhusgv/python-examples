#This program will generate a brand name based on user input

#Greet the user
print("\nWelcome, we will generate a brand name for you.\n")

#Get the user location
location = input("Where are you from? \n")

#Get the name of the pet
petname = input("What is the name of your pet? \n")

Bandname = location+petname
#Print the band name
print(f'The band name is {Bandname}\n')
