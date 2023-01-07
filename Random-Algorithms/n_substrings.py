def nSubStrings(str, n):
    # List comprehension to get the substrings
    substrings = [string[i:i+n] for i in range(len(string) - n + 1)]
    return substrings


# String from which to get the substrings
string = "abcdefg"
# Length of the substrings
n = 2
substrings = nSubStrings(string, n)
# Print the list of substrings
print(substrings)

