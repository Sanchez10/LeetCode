from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        output = []
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted in anagram:
                anagram[word_sorted].append(word)
            else:
                anagram[word_sorted] = [word]
        
        for group in anagram.values():
            output.append(group)
        
        return output
    
if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs1 = [""]
    print(s.groupAnagrams(strs1)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
