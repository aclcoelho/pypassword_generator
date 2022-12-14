import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#ONE POSSIBLE VERSION
# #Getting a random list of letters based on user input
# random_letters = random.sample(letters, nr_letters)
# #Getting a random list of numbers based on user input
# random_numbers = random.sample(numbers, nr_numbers)
# #Getting a random list of symbols based on user input
# random_symbols = random.sample(symbols, nr_symbols)
# #Adding the lists together
# final_list = random_letters + random_numbers + random_symbols
# #Getting the total length of how long the password should be
# total_length = nr_letters + nr_numbers + nr_symbols
# #Getting a random list out of final list
# ordered_list = random.sample(final_list, total_length)
# #Transforming the list into a string
# print("".join(ordered_list))

#SECOND POSSIBLE VERSION
password = []

for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

final_list = "".join(random.sample(password, nr_letters+nr_numbers+nr_symbols))
print(f"Your password is: {final_list}")