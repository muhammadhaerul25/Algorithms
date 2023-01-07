from itertools import combinations

def allCombinations(arr):
    # Loop through the range of length of the combinations
    comb = []
    for r in range(1, len(arr)+1):
    # Get all combinations of length r
        comb += combinations(arr, r)
    return comb

numbers = [1, 2, 3, 4]
comb = allCombinations(numbers)
for c in comb:
    print(c)