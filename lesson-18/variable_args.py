def args_function(*args):
    print(type(args))

    print(args[0])

def my_function(**kwargs):
    print(type(kwargs))

    for key in kwargs:
        print(key)

    for item in kwargs.items():
        print(item)

    print(kwargs["value"])


def add_player(**settings):
    if "level" in settings:
        print(settings["level"])
    else:
        print("No level provided, defaulting to 1")
        settings["level"] = 1


# add_player(player_name="Rod", class_name="Accountant")
# add_player(player_name="Rod1227", class_name="Accountant", level=100)

def order_summary(*items, **options):
    print("Items ordered:")
    for item in items:
        print("-", item)
        print("Options:")
    for key, value in options.items():
        print(f"{key}: {value}")
    
# order_summary("burger", "fries", drink="cola", size="large")
# order_summary("burger", cheese="extra")

def get_user(player_id, screen_name):
    print(f"{player_id}: {screen_name}")

player = ("asdlkja", "Rod1227")

# get_user(*player)

dict_player = {
    "player_id": "alsdkjasd",
    "screen_name": "Rod1227",
}

get_user(**dict_player)