# definition
burger = {
    "patties": 1,
    "patty_type": "beef",
    "cheese": True,
    "toppings": ["lettuce", "tomato", "onion", "mayonnaise", "peanut butter"],
    "bun": "sesame seed"
}

# access

burger["patties"]

# add a new key
burger["cooked"] = "rare"


# error
#burger["no key :()"]

# check if key exists
if "patties" in burger:
    print("Key exists!")
else:
    print("Key does not exist :(")

# safe getter

burger.get("key that doesn't exist", None)

burger_menu = {
    "elvis": burger.copy(),
    "standard": burger.copy(),
    "veggie": {
        "patties": 2,
        "patty_type": "veggie",
        "cheese": False,
        "toppings": ["peanut butter"],
        "bun": "whole wheat"
    }
}

burger_menu["elvis"]["patties"] = 0

print(burger_menu)