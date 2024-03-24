class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dict = { 
            "I": 1, "IV": 4, "V": 5, "IX": 9,
            "X": 10, "XL": 40, "L": 50, "XC": 90,
            "C": 100, "CD": 400, "D": 500, "CM": 900,
            "M": 1000
        }
        int_number = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in conversion_dict:
                int_number += conversion_dict[s[i:i+2]]
                i += 2
            else:
                int_number += conversion_dict[s[i]]
                i += 1
        return int_number

if __name__ == "__main__":
    access_solution = Solution()
    s = "CMLII"
    print(access_solution.romanToInt(s))

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
