class Solution(object):
    def lengthOfLastWord(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])

if __name__ == "__main__":
    s = Solution()
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"
    print(s.lengthOfLastWord(s2))
    