# Password Generator

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '9']
symbols = ['!', '#', '/', '(', ')', '*', '+']


print("Welcome  to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password \n"))
nr_numbers = int(input("How many numbers would you like in your password \n"))
nr_symbols = int(input("How many symbols would you like in your password \n"))

rand_let = random.sample(letters, nr_letters)
rand_num = random.sample(numbers, nr_numbers)
rand_sym = random.sample(symbols, nr_symbols)

total_num = nr_letters + nr_numbers + nr_symbols

easy_password = rand_let + rand_num + rand_sym
# print("".join(easy_password))

hard_password = random.sample(easy_password, total_num)
# print("".join(hard_password))

#random.shuffle(easy_password)
# print(easy_password)
# print("".join(easy_password))

print(f"Your password is '{"".join(easy_password)}' or '{"".join(hard_password)}' or '{"".join(easy_password)}'")