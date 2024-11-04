class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_letters = {}
        for idx, letter in enumerate(s):
            if letter not in count_letters:
                count_letters[letter] = (idx, 1)
            else:
                _ , sum = count_letters.get(letter)
                count_letters[letter] = (idx, sum+1)
        
        for ch, val in count_letters.items():
            if val[1] == 1:
                return val[0]
        return -1

if __name__ == "__main__":
    access_solution = Solution()
    s = "leetcode"
    s1 = "loveleetcode"
    s2 = "aabb"
    print(access_solution.firstUniqChar(s))
