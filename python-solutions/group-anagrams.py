from collections import defaultdict
from typing import List

# using unique keys, not sorting


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a default dictionary that will fall back to a list when accessing
        # a key that doesn't exist, this allows for an array to be appended to
        # when writing to a key that hasn't been initialized yet.
        ans = defaultdict(list)
        for s in strs:
            # Make an array the size and put an zero for each element of the array
            count = [0] * 26
            for c in s:
                # get the unicode value and subtract the unicode for a, which will result in a range of 0 - 25 as the key
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()
