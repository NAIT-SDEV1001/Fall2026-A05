print("Golf Score Calculator")
count = 0
total_score = 0

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        try:
            total_score += int(user_input)
            count += 1
        except ValueError as error_message:
            print(f"Could not convert {user_input} to a number. ({error_message})")


# only calculate the average if we have at least one score

# if count > 0:
#     average = total_score / count
#     print(f"Your average golf score is {average}.")
# else:
#     print("No scores entered.")

try:
    average = total_score / count
    print(f"Your average golf score is {average}.")
except ZeroDivisionError:
    print("You didn't enter any scores!")