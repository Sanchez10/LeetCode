class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string_lenght = 0
        for i in range(len(s)):
            new_string = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in new_string:
                    new_string += s[j]
                else:
                    break

            if len(new_string) > max_string_lenght:
                max_string_lenght = len(new_string)

        return max_string_lenght

if __name__ == "__main__":
    access_solution = Solution()
    s = "abcabcbb"
    s1 = "bbbbb"
    s2 = "pwwkew"
    print(access_solution.lengthOfLongestSubstring(s2))
