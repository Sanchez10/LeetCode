from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count_words = 0
        for word in words:
            how_many_letters = 0
            for letter in word:
                if letter in allowed:
                    how_many_letters += 1
            if how_many_letters == len(word):
                count_words += 1
        return count_words
    
if __name__ == "__main__":
    access_solution = Solution()
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    allowed1 = "abc"
    words1 = ["a","b","c","ab","ac","bc","abc"]
    allowed2 = "cad"
    words2 = ["cc","acd","b","ba","bac","bad","ac","d"]
    print(access_solution.countConsistentStrings(allowed2, words2))
