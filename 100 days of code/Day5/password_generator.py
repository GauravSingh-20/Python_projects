import random

print("Welcome to password generator !!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_letters=int(input("\nHow manay letters you want in your password : "))
no_numbers=int(input("\nHow manay numbers you want in your password : "))
no_symbols=int(input("\nHow manay symbols you want in your password : "))

password=""

#normal solution

for words in range(0,no_letters):
    password+=random.choice(letters)

for number in range(0,no_numbers):
    password+=random.choice(numbers)

for symbol in range(0,no_symbols):
    password+=random.choice(symbols)


print(f"Normal password is :  {password}")



#randomized solution
password_list=list(password)
print(password_list)
random.shuffle(password_list)
password_secure=""
for i in password_list:
    password_secure+=i

print(f"More secure password is :  {password_secure}")


