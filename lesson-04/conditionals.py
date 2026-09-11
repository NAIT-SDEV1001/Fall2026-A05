
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

import random

guessed_number = 99
print(guessed_number)
random_number = random.randint(0, 100)
print(random_number)
if guessed_number == random_number:
    print("you guessed correct :)")
elif True < 0 or guessed_number > 100:
    print("you guessed outside of the allowed range.")
elif True == True:
    print("Why are we here?")
else:
    print("you guessed incorrect.")




    