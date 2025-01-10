from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[0:m+n] = sorted(nums1[:m]+nums2[:n])
        print(nums1)
        return None
        

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0] 
    m = 3
    nums2 = [2,5,6]
    n = 3

    nums11 = [0]
    m1 = 0
    nums21 = [1]
    n1 = 1
    print(s.merge(nums11, m1, nums21, n1))
        