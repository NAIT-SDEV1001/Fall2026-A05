class PokemonType:
    def __init__(self) -> None:
        pass

class GrassType(PokemonType):
    def __str__(self):
        return "Grass"

class PoisonType(PokemonType):
    def __str__(self):
        return "Poison"

class FireType(PokemonType):
    def __str__(self):
        return "Fire"

class WaterType(PokemonType):
    def __str__(self):
        return "Water"

class Pokemon:
    def __init__(self, species: str, *type: PokemonType) -> None:
        self.species = species
        self.type = type

    def __str__(self):
        output = ""
        for t in self.type:
            output += f"{t}\n"

        return output

    def execute_attack(self) -> None:
        print(f"{self.species} attacked!")
        
class Team:
    def __init__(self, *pokemon: Pokemon):
        self.pokemon = pokemon

    def __str__(self) -> str:
        output = ""

        for p in self.pokemon:
            output += f"{p.species}\n"

        return output

grass = GrassType()
poison = PoisonType()
fire = FireType()
water = WaterType()

bulbasaur = Pokemon("bulbasaur", grass, poison)
squirtle = Pokemon("squirtle", water)
charmander = Pokemon("charmander", fire)

team_a = Team(bulbasaur, squirtle, charmander)

for pokemon in team_a.pokemon:
    print(pokemon)