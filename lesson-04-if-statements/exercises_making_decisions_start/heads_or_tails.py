import random as rng

user_guess = input("Guess the coin flip! Enter heads or tails (h/t):")

random_number = rng.randint(0, 1)

if random_number == 0:
    print("The coin flip was: heads")
else:
    print("The coin flip was: tails")

if (user_guess == "h" and random_number == 0) or (user_guess == "t" and random_number == 1):
    print("You guessed correct")
else:
    print("You guessed incorrect")