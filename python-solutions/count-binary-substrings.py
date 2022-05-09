class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevGroupCount = 0
        currGroupCount = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prevGroupCount, currGroupCount)
                prevGroupCount, currGroupCount = currGroupCount, 1
            else:
                currGroupCount += 1

        return ans + min(prevGroupCount, currGroupCount)
