from typing import List

class Solution(object):
    def rotate(self, nums: List[list], k: int) -> None:
        n = len(nums)
        if n <= 1 or k == 0:
            nums[:] = nums
        else:
            k %= n
            print(k)
            nums[:] = nums[-k:] + nums[:-k]
            print(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3 
    nums1 = [-1,-100,3,99] 
    k1 = 2
    nums2 = [1]
    k2 = 0
    nums3 = [1,2]
    k3 = 3
    nums4 = [1,2]
    k4 = 5
    nums5 = [1,2]
    k5 = 1
    nums6 = [1,2,3]
    k6 = 4
    s.rotate(nums6, k6)
