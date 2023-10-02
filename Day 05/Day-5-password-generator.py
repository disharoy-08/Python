#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Eazy Level - Oredr not randomized:
# letter_list = []
# for i in range(0, nr_letters):
#   r_letter = random.randint(0, len(letters)-1)
#   letter_list.append(letters[r_letter])
# print(letter_list)

# symbol_list = []
# for i in range(0, nr_symbols):
#   s_letter = random.randint(0, len(symbols)-1)
#   symbol_list.append(symbols[s_letter])
# print(symbol_list)

# numbers_list = []
# for i in range(0, nr_numbers):
#   n_letter = random.randint(0, len(numbers)-1)
#   numbers_list.append(numbers[n_letter])
# print(numbers_list)

# list = letter_list + symbol_list + numbers_list
# print(list)

# # password = ""
# # for chart in list:
# #   password = password + chart
# # print(password)                #Eazy Step Done

# password = ""
# for numb in range (0, len(list)):
#   index = random.randint(0, len(list)-1 )
#   password = password + list[index]
# print(password)

# Eazy Level
# password = ""
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
