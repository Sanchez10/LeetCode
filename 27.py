from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return nums
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    nums1 = [0,1,2,2,3,0,4,2]
    val1 = 2
    print(s.removeElement(nums1, val1))
