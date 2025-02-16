class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps


if __name__ == "__main__":
    s = Solution()
    num = 14
    num1 = 8
    num2 = 123
    print(s.numberOfSteps(num))
