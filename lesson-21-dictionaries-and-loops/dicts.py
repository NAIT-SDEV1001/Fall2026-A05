player_ability = {
    "name": "Student punching",
    "description": "Teachin' em a lesson",
    "cost": 100
}

# foreach each
for key in player_ability.keys():
    print(f"{key}: {player_ability[key]}")

# foreach key
for prop in player_ability:
    print(f"{prop}: {player_ability[prop]}")

# foreach value
for value in player_ability.values():
    print(value)

# foreach key-value pair
for kvp in player_ability.items():
    print(kvp)

sorted_dictionary = sorted(player_ability)
print(sorted_dictionary)

inventory = {"apples": 5, "bananasssss": 2, "oranges": 8}

for fruit, count in sorted(inventory.items(), key=len):
    print(f"{fruit.title()}: {count}")