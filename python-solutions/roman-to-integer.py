class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                  "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
                  }
        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in digits:
                result += digits.get(s[i:i+2])
                i += 1
            else:
                result += digits.get(s[i])
            i += 1
        return result
