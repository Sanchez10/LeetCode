from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        number_of_pairs = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if i < j and j < n:
                    if (nums[i] + nums[j]) < target:
                        number_of_pairs += 1
        return number_of_pairs
    
if __name__ == "__main__":
    access_solution = Solution()
    nums = [-1,1,2,3,1]
    target = 2
    nums1 = [-6,2,5,-2,-7,-1,3]
    target2 = -2
    print(access_solution.countPairs(nums1, target2))
