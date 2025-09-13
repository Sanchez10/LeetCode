from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        qtt_numbers = 1
        for fast in range(1, len(nums)):
            if nums[slow] == nums[fast]:
                qtt_numbers += 1
                if qtt_numbers == 2:
                    nums[slow+1] = nums[fast]
                    slow += 1
            else:
                qtt_numbers = 1
                nums[slow+1] = nums[fast]
                slow += 1

        print(nums[:slow+1])
        return len(nums[:slow+1])
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    nums1 = [0,0,1,1,1,1,2,3,3]
    nums2 = [1]
    nums3 = [1,1,1,1,2,2,3]
    print(s.removeDuplicates(nums3))
