from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
    
if __name__ == "__main__":
    solution = Solution()
    words = ["abc","car","ada","racecar","cool"]
    words1 = ["notapalindrome","racecar"]
    words2 = ["def","ghi"]
    print(solution.firstPalindrome(words2))