from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set.intersection(nums2_set))

if __name__ == "__main__":
    access_solution = Solution()
    nums1 = [4,2,1]
    nums2 = [4,4,5]
    print(access_solution.intersection(nums1, nums2))
