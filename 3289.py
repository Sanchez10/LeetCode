from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        two_sneaky = {}
        eliminated_sneaky = []
        for num in nums:
            if two_sneaky.get(num):
                eliminated_sneaky.append(num)
            else:
                two_sneaky[num] = 1
            
            if len(eliminated_sneaky) == 2:
                return eliminated_sneaky
        
        return eliminated_sneaky
    
if __name__ == "__main__":
    access_solution = Solution()
    nums = [0,1,1,0]
    nums1 = [0,3,2,1,3,2]
    nums2 = [7,1,5,4,3,4,6,0,9,5,8,2]
    print(access_solution.getSneakyNumbers(nums2))
