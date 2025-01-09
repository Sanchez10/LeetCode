from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        qntd = 0
        for word in words:
            if word.startswith(pref):
                qntd += 1
        return qntd
    
if __name__ == "__main__":
    s = Solution()
    words = ["pay","attention","practice","attend"]
    pref = "at"
    words1 = ["leetcode","win","loops","success"]
    pref1 = "code"
    print(s.prefixCount(words1, pref1))
