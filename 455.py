from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children_with_cookie = 0
        child_pointer = 0
        cookie_pointer = 0
        while child_pointer < len(g) and cookie_pointer < len(s):
            if s[cookie_pointer] >= g[child_pointer]:
                children_with_cookie += 1
                child_pointer += 1
            cookie_pointer += 1
        return children_with_cookie

if __name__ == "__main__":
    access_solution = Solution()
    g = [1,2,3,4]
    s = [4,2,3,4]
    print(access_solution.findContentChildren(g, s))
