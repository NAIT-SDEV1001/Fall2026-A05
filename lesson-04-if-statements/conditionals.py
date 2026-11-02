
# user_name = input("name?")
# password = input("password?")

# if user_name != "dominic":
#     print("Logged in")
# else:
#     print("Not logged in, something went wrong")

# Equals ==
# Not equals !=
# >
# <
# <=
# >=

# import random

# guessed_number = 101
# print(guessed_number)
# random_number = random.randint(0, 100)
# print(random_number)

# if guessed_number >= 0 and guessed_number <= 100:
#     print("you guessed inside of the allowed range.")

#     if guessed_number == random_number:
#         print("you guessed correct :)")
#     else:
#         print("you guessed incorrect.")

#     print("1")

# print("2")

import random
 
guessed_number = input("guess a number from 0-100")
 
random_number = random.randint(0, 100)

guessed_int = int(guessed_number)


if guessed_int >= 0 and guessed_int <= 100:
    print("you guessed inside the normal range :O")
 
    if guessed_int == random_number:
        print("you guessed correct :)")
    else:
        print("you guessed incorrect :(")

my_bool = False