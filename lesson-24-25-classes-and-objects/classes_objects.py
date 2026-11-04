class Pokemon:
    def __init__(self, species: str, cry: str) -> None:
        self.species = species
        self.unique_cry = cry
        self.max_health = 10
        self.current_health = 7
        self.abilities = []

    def __str__(self) -> str:
        return f"{self.species}, {self.unique_cry}, {self.max_health}, {self.current_health}"

    def __repr__(self) -> str:
        return f'Pokemon(make="{self.species}", cry="{self.unique_cry}")'

    def add_ability(self):
        self.abilities = Ability()
        
    def cry(self) -> None:
        print(f"{self.species} said {self.unique_cry}")

    def get_species(self) -> str:
        return self.species

    def get_health_as_percent(self) -> float:
        as_a_percent: float = self._current_health / self._max_health
        return as_a_percent

class Ability:
    def __init__(self):
        pass

class Trainer:
    def __init__(self) -> None:
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        self.pokemon.append(pokemon)

    def __str__(self) -> str:
        output = "Trainers pokemon: \n"

        for pokemon in self.pokemon:
            output += f"- {pokemon.species} \n"

        return output

    def find_pokemon(self, species: str) -> Pokemon | None:
        pass

trainer = Trainer()

bulbasaur = Pokemon("Bulbasaur", "BRrrrr")
squirtle = Pokemon("Squirtle", "Squort")
charmander = Pokemon("Charmander", "Raaahr")

trainer.add_pokemon(bulbasaur)
trainer.add_pokemon(squirtle)
trainer.add_pokemon(charmander)

found_pokemon = trainer.find_pokemon("Ditto")

print(trainer)

# bulbasaur.cry()
# squirtle.cry()
# charmander.cry()
# print(bulbasaur)