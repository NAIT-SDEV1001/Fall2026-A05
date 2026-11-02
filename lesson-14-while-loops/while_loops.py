# print("Enter numbers to add. Type 'done' to finish.")
# total = 0

# done = False

# while done:
#     value = input("Enter a number: ")
    
#     if value == "done":
#         break

#     total += int(value)

# print(f"Total sum: {total}")

# keep_going = True

# while keep_going:
#     answer = input("Keep going? (y/n): ")

#     if answer == "n":
#         keep_going = False

# print("Loop ended.")

number_to_guess = 10

while True:
    user_guess = input("Enter your guess: ")
    
    try:
        number_guessed = int(user_guess)
        if number_guessed == number_to_guess:
            print("You win!")
            break
        else:
            print("Wrong!")
    except:
        print("Number you guessed is invalid.")
