from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for number in nums:
            if number % 3 == 0:
                continue
            if (number + 1) % 3 == 0 or (number - 1) % 3 == 0:
                operations += 1
        return operations

if __name__ == "__main__":
    access_solution = Solution()
    nums = [1,2,3,4]
    nums1 = [3,6,9]
    print(access_solution.minimumOperations(nums1))
