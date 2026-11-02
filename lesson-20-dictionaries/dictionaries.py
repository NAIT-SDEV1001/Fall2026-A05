player = {
    "abilities": ["Punch", "Build", "DoubleJump", "Eat"],
    "max_health": 100,
    "face_id": 50,
}

# ability = input("Ability to check: ")

# if ability in player["abilities"]:
#     print("You can do it!")

player["current_health"] = 100
print(player)

for key in player:
    print(f"{key}: {player[key]}")

for item in player.items():
    print(item)

for value in player.values():
    print(value)

print(player.get("level", -1))

for key in player:
    print(f"{key}: {player[key]}")

player["guild_id"] = 10

if "guild_id" in player:
    print("Player is in a guild")
else:
    print("Player is not in a guild")

# player = {
#     "abilities": ["Punch", "Build", "DoubleJump", "Eat"],
#     "max_health": 100,
#     "face_id": 50,
# }

player.pop("max_health")

player["stats"] = {}

player["stats"]["max_health"] = 100
player["stats"]["max_mana"] = 100
player["stats"]["xp"] = 100
player["stats"]["strength"] = 100
player["stats"]["agility"] = 100
player["stats"]["defense"] = 100

player["inventory"] = []

sword = {
    "name": "Super Sword"
}

health_potion = {
    "name": "Pot",
    "amount": 50,
}

player["inventory"].append(sword.copy())
player["inventory"].append(health_potion.copy())

damage_effect = {
    "health": -5
}

stun_effect = {
    "duration": 6
}

ability = {
    "name": "Punch",
    "effects": [damage_effect, stun_effect]
}