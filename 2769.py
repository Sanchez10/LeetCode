class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
    
if __name__ == "__main__":
    solution = Solution()
    num = 4
    t = 1
    num1 = 3
    t1 = 2
    print(solution.theMaximumAchievableX(num1, t1))
