import random


print("Welcome to the password generator")
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 
           'o', 'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
           'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
symbols = ['!','<','>','@','#','$','&','%','^','*','(',')','-','_','~','=',
           '+','/']


#EASY LEVEL
""" password = ""
for char in range(1, length_of_numbers + 1):
    password += random.choice(numbers)
    
for char in range(1, length_of_letters + 1):
    password += random.choice(letters)
    
for char in range(1, length_of_symbols + 1):
    password += random.choice(symbols)
    
print(password) """

#HARD LEVEL

while True:
    length_of_numbers = int(input('How many numbers will you want?:'))
    length_of_letters = int(input('How many letters will you want?:'))
    length_of_symbols = int(input('How many symbols will you want?:'))

    password_list = []

    for char in range(1, length_of_numbers + 1):
        password_list.append(random.choice(numbers))
        
    for char in range(1, length_of_letters + 1):
        password_list.append(random.choice(letters))
        
    for char in range(1, length_of_symbols + 1):
        password_list.append(random.choice(symbols))
        
    #print(password_list)
    random.shuffle(password_list)
    #print(password_list)
    password = ""
    for char in password_list:
        password += char
    print("Your password is: " + password)
    
    again = input("Do you want to generate another password? Type 'y' or 'n'").lower()
    if again != 'y':
        break
