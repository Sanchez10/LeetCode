"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
- 1 <= haystack.length, needle.length <= 104
- haystack and needle consist of only lowercase English characters.
"""

# Topics
# - Two Pointers
# - String
# - String Matching

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle) 
        return index

if __name__ == "__main__":
    haystack = "sadbutsad" 
    needle = "sad"
    haystack1 = "leetcode"
    needle1 = "leeto"
    haystack2 = "mississippi"
    needle2 = "issip"

    solution = Solution()
    print(solution.strStr(haystack1, needle1))
