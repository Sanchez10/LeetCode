from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1

if __name__ == "__main__":
    access_solution = Solution()
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    print(access_solution.search(nums2, target2))
