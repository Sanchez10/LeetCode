class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expanded_around_center(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        start = 0
        end = 0
        for i in range(len(s)):
            odd = expanded_around_center(s, i, i)
            even = expanded_around_center(s, i, i+1)
            max_lenght = max(odd, even)
            if max_lenght > end - start:
                start = i - (max_lenght-1)//2
                end = i + max_lenght//2

        return s[start:end+1]    

if __name__ == "__main__":
    access_solution = Solution()
    s = "babad"
    s1 = "cbbd"
    s2 = "a"
    s3 = "bb"
    print(access_solution.longestPalindrome(s3))
