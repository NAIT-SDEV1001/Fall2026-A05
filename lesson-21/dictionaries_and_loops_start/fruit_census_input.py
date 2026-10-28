from fruit_census_utils import tally_results
from fruit_census_utils import print_results

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
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}




results = tally_results(fav_fruit_voters)

while True:
    vote = input("Banana, apple or orange? (Q to quit)").lower()

    if vote == "q":
        break

    try:
        results[vote] += 1
    except KeyError as e:
        print(f"Not a valid option: {e}")

print_results(results)