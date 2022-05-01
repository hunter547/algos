# Algorithm: The Sliding Window
# Problem: Given a string of characters, find the longest substring of
#          of non repeating characters  

def slidingWindow(s: str) -> int:
    seen = {}
    i = 0
    ans = 0
    for j in range(len(s)):
        # This character has been encountered in the string before
        if s[j] in seen:
            # Since this character has been encountered in the string before,
            # i needs to either stay at its current position if the encountered
            # character came before it, or be moved to the index where it
            # last seen (plus 1, so that the next character starts the unique char string)
            i = max(seen[s[j]], i)
        # ans is assigned the larger of its current amount or the difference between
        # i and j (plus 1 to convert from the zero based nature of arrays)
        ans = max(ans, j - i + 1)
        # Set the key of the seen charater in the map to the index + 1 of where if was found
        # this ensures that if its seen again, i can move to that position if the index is
        # higher than i's current position
        seen[s[j]] = j + 1
    return ans

# Execute test

# abcabcdabab should return 4 for "abcd"
print(slidingWindow('abcabcdabab'))