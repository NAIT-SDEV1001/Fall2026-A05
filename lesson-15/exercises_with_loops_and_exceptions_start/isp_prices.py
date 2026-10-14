user_input = input("Enter the package: ")
input_hours = 0
total_cost = 0
 
try:
        input_hours = float(input("Enter the number of hours used: "))
except ValueError as error_message:
        print("Please enter a valid number of hours")
 
 
if user_input == "A":
        total_cost = 9.95
        if input_hours > 10:
                total_cost = 9.95+(float(input_hours)-10)*2
elif user_input == "B":
        total_cost = 13.95
        if input_hours > 20:
                total_cost = 13.95+(input_hours-20)*1
elif user_input == "C":
        total_cost = 19.95
else:
        print("Not a valid plan")
 
 
print(f"The total price is ${total_cost}")