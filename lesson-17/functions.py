def calculate_damage(amount, damage_type):
    print(f"{amount} point of {damage_type} damage")

def grant_experience(amount, multiplier, heal_on_level_up, player_id):
    print(f"{amount * multiplier} xp granted to {player_id}, heal? {heal_on_level_up}")