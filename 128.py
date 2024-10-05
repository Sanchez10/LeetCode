from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

if __name__ == "__main__":
    access_solution = Solution()
    array1 = [100,4,200,1,3,2]
    array2 = [0,3,7,2,5,8,4,6,0,1]
    access_solution.longestConsecutive(array1)
