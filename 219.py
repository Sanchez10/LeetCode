from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_idx = {}

        for idx, value in enumerate(nums):
            if value in value_idx and abs(idx - value_idx[value] ) <= k:
                    return True
            else:
                value_idx[value] = idx

        return False
    
if __name__ == "__main__":
    access_solution = Solution()
    nums = [1,2,3,1]
    k = 3
    nums1 = [1,0,1,1]
    k1 = 1
    nums2 = [1,2,3,1,2,3]
    k2 = 2
    print(access_solution.containsNearbyDuplicate(nums, k))
