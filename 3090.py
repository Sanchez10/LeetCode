class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_substring_lenght = 1
        qnt_letters = {}
        l, r = 0, 0

        qnt_letters[s[0]] = 1
        while r < len(s) - 1:
            r += 1
            if qnt_letters.get(s[r]):
                qnt_letters[s[r]] += 1
            else:
                qnt_letters[s[r]] = 1
            
            while qnt_letters[s[r]] == 3:
                qnt_letters[s[l]] -= 1
                l += 1

            max_substring_lenght = max(max_substring_lenght, r - l + 1)
        
        return max_substring_lenght

if __name__ == "__main__":
    access_solution = Solution()
    s = "bcbbbcba"
    s1 = "aaaa"
    s2 = "acedc"
    print(access_solution.maximumLengthSubstring(s2))
    