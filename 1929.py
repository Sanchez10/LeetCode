from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans
    
if __name__ == "__main__":
    access_solution = Solution()
    # test1 = [1,2,1]
    test2 = [1,3,2,1]
    access_solution.getConcatenation(test2)
