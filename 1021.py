class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = ""
        flag = True
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1

            if count == 1 and flag is True:
                flag = False
                continue
            if count == 0 and flag is False:
                flag = True
                continue

            ans += s[i]
        return ans

if __name__ == "__main__":
    access_solution = Solution()
    s = "(()())(())"
    s1 = "(()())(())(()(()))"
    s2 = "()()"
    print(access_solution.removeOuterParentheses(s1))