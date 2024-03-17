class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        palindrome = test[::-1]
        return True if test == palindrome else False

if __name__ == "__main__":
    access_solution = Solution()
    x = 10
    print(access_solution.isPalindrome(x))
