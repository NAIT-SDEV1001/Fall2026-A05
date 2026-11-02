def tally_results(votes):
    '''
    Tallies the results of votes, returns a dictionary of voting results
    '''
    results = {}

    for vote in votes.values():
        # we should make sure value is a valid key in voting results
        results[vote] += 1

    return results

def print_results(results):
    for key, value in results.items():
        print(f"{key}: {value}")