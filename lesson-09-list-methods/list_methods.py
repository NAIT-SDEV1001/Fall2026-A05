pokemon = ["Falinx", "Mewtwo", "Blastoise", "Magikarp"]

# for i in range(0, len(pokemon)):
#     print(pokemon[i])

# print("----")

# pokemon.sort()

# for i, value in enumerate(pokemon):
#     print(pokemon[i])

# pokemon.sort(reverse=True)
# print("----")

# print(pokemon)

# pokemon.append("Zapdos")
# pokemon.append("Alakazam")

# print(pokemon)

# pokemon.sort()

# print(pokemon)
# pokemon.insert(500, "Charmander")
# print(pokemon)

# # default removes the last value, or we can provide an index
# item_removed = pokemon.pop(1)
# print(item_removed)
# print(pokemon)
# print("----")
# does_mewtwo_exist = "Mewtwo" in pokemon
# print(does_mewtwo_exist)
# pokemon.remove("Mewtwo")
# print(pokemon)

pokemon_to_remove = ["Squirtle", "Wartortle", "Blastoise"]

# for each pokemon in pokemon_to_remove
    # if the pokemon exists in our original list
        # remove it from the pokemon list

# pokemon = original list

print(pokemon)

for i,pokemon_name in enumerate(pokemon_to_remove):
    print("Checking for:" + pokemon_name)
    if pokemon_name in pokemon:
        print("Found " + pokemon_name)
        pokemon.remove(pokemon_name)

print(pokemon)