days_playing_squash = 2
time_machine_days_added = 3
time_warp_multiplier = 2
slowing_spell_divisor = 7

# Math Order of Operations
user_input_days = input("How many days until the newest assignment is due? ")

days_until_newest_assignment_due = int(user_input_days)


special_remainder_power = 2
# Reassign days_until_assignment_due to all of the operations we did above.
days_until_newest_assignment_due = (( days_until_newest_assignment_due -
                              days_playing_squash +
                              time_machine_days_added) * time_warp_multiplier // slowing_spell_divisor
                              ) ** special_remainder_power

print("We did the same thing as before, but in one line: ")
print(f"Newest Assignment due in {days_until_newest_assignment_due} perceived days")