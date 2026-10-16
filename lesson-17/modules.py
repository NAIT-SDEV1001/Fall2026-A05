# from functions import my_function

# my_function()

from functions import calculate_damage
from functions import grant_experience

calculate_damage(1, "normal")

grant_experience(100, 2, player_id="Player_One", heal_on_level_up=False)
grant_experience("Player_One", multiplier=2, heal_on_level_up=False, player_id="Player_One")