class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_strings = 0
        i = 0
        for j in range(2, len(s)):
            repeated_letter = {}
            for letter in s[i:j+1]:
                if repeated_letter.get(letter):
                    repeated_letter[letter] += 1
                else:
                    repeated_letter[letter] = 1
            
            if 2 not in repeated_letter.values() and 3 not in repeated_letter.values():
                good_strings += 1

            i += 1
            j += 1
            
        return good_strings
    
if __name__ == "__main__":
    access_solution = Solution()
    s = "xyzzaz"
    s1 = "aababcabc"
    s2 = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
    print(access_solution.countGoodSubstrings(s2))
