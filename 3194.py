from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average = []
        for _ in range(len(nums) // 2):
            max_number = nums.pop(nums.index(max(nums)))
            min_number = nums.pop(nums.index(min(nums)))
            average.append((max_number + min_number) / 2)
        return min(average)
    
if __name__ == "__main__":
    solution = Solution()
    nums = [7,8,3,4,15,13,4,1]
    nums1 = [1,9,8,3,10,5]
    nums2 = [1,2,3,7,8,9]
    print(solution.minimumAverage(nums2))
