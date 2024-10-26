class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i]) - ord(s[i+1]))
        return sum
    
if __name__ == "__main__":
    access_solution = Solution()
    s = "hello"
    s1 = "zaz"
    print(access_solution.scoreOfString(s1))
