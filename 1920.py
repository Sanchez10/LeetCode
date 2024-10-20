from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)):
            ans.append(nums[nums[index]])
        return ans
    
if __name__ == "__main__":
    access_solution = Solution()
    test1 = [0,2,1,5,3,4]
    test2 = [5,0,1,2,3,4]
    out = access_solution.buildArray(test2)
    print(out)
