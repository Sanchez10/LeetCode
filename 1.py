from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

if __name__ == "__main__":
    access_solution = Solution()
    test = [3,3]
    target = 6
    print(access_solution.twoSum(test, target))
