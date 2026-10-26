fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
    "dominic": "fresh meat",
    "tristan": "fresh meat",
    "ethan": "bat meat"
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

for vote in enumerate(fav_fruit_voters):
    print(vote)

# for vote in fav_fruit_voters.values():
#     voting_results[vote] += 1

print(f"Results: \n {voting_results}")

# total_votes = 0
# for count in voting_results.values():
#     total_votes += count

# print(total_votes)

# for fruit, votes in voting_results.items():
#     print(F"- The fruit: {fruit} has {votes} votes")

custom_order = [
    "john",
    "jessie",
    "daniel",
    "michael",
    "jessica",

    #...
]

for name in custom_order:
    print(f"{name}: {fav_fruit_voters[name]}")