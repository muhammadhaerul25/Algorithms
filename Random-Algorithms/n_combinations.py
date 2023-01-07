from itertools import combinations

def nCombinations(arr, n):    
    # Get all combinations of length n
    comb = combinations(arr, n)
    return comb


numbers = [1, 2, 3, 4]
comb = nCombinations(numbers, 2)

# Print the combinations
for c in comb:
    print(c)

