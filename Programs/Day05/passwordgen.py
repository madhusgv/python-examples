import random
import string

print("Welcome to pyPassword Generator!")
pwdlen = int(input("How many letters would you like in your password? : "))
symbollen = int(input("How many synbols would you like in your password? : "))
numlen = int(input("How many numbers would you like in your password? : "))

password = ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_letters, k=pwdlen))
print(password)

