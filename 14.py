"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "". 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs.pop()
        print(longest_prefix)

        if longest_prefix == '':
            return ''

        for word in strs:
            if word == '':
                return ''
            
            for i in range(len(longest_prefix)):
                if i >= len(word):
                    longest_prefix = longest_prefix[:i]
                    break
                
                if longest_prefix[i] != word[i]:
                    longest_prefix = longest_prefix[:i]
                    break

        return longest_prefix
    
if __name__ == "__main__":
    s = Solution()
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = ["","b"]
    strs4 = ["aaa","aa","aaa"]
    print(s.longestCommonPrefix(strs4))
