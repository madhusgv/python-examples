#This program get your current age and calculate and show you
#how many days, weeks and years of your life, if you live 90 years

#Literals
days   = 365
months = 12
weeks  = 52
age_limit_years = 90

#Get the age
current_age = int(input("What is your current age? "))

age_limit_months = age_limit_years*months
age_limit_weeks = age_limit_years*weeks
age_limit_days = age_limit_years*days

if (current_age > age_limit_years):
   print("You are living more than expected. Good Luck\n")
   exit(0)

remaining_age_years  = age_limit_years - current_age
remaining_age_months = remaining_age_years*months
remaining_age_weeks  = remaining_age_years*weeks
remaining_age_days   = remaining_age_years*days

print(f'Your remaing years : {remaining_age_years}, months: {remaining_age_months}, weeks: {remaining_age_weeks}, days: {remaining_age_days}\n')