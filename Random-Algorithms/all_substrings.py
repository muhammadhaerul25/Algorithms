def allSubStrings(str):
    # List comprehension to get the substrings
    substrings = [string[i:i+n] for n in range(1, len(string)+1) for i in range(len(string) - n + 1)]
    return substrings


# String from which to get the substrings
string = "abcdefg"
substrings = allSubStrings(string)
# Print the list of substrings
print(substrings)
