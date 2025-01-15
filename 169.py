from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_numbers = {}
        for num in nums:
            if num not in count_numbers: 
                count_numbers[num] = 1     
            else:
                count_numbers[num] += 1 
        
        for key, value in count_numbers.items():
            if value > (n/2):
                return key
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,2,3]
    nums1 = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums1))
