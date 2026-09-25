# Lists and Loops


days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_of_weekend = ("Saturday", "Sunday")

print("Days of the week are")

for index, day in enumerate(days_of_week):
    if day == "Wednesday":
        break

    if day in days_of_weekend:
        print(f"{day} is a weekend day")
    else:
        print(f"{day} is a weekday")

