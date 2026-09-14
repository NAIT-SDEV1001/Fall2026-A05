day = input("Enter a day of the week: ").lower()

match day:
    case "monday":
        print("Start of the work week!")
    case "friday":
        print("Almost the weekend!")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case "saturday":
        print("It's saturday")
    case _:
        print("Just another day.")