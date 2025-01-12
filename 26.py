from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        print(nums[:unique_index+1])
        return unique_index + 1

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    nums2 = [1]
    nums3 = [1,1]
    print(s.removeDuplicates(nums1))
