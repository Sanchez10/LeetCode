from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        sn1 = set(nums1)
        sn2 = set(nums2)
        intersection = sorted(sn1.intersection(sn2))
        if intersection: 
            return intersection[0]
        else:
            return -1

if __name__ == "__main__":
    access_solution = Solution()
    nums1 = [4,2,1]
    nums2 = [4,4,5]
    print(access_solution.getCommon(nums1, nums2))
