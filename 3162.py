from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        number_of_good_pairs = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                rest_division = nums1[i] % (nums2[j] * k)
                if not rest_division:
                    number_of_good_pairs += 1
        return number_of_good_pairs
    
if __name__ == "__main__":
    solution = Solution()
    # nums1 = [1,3,4]
    # nums2 = [1,3,4]
    # k = 1
    nums1 = [1,2,4,12]
    nums2 = [2,4]
    k = 3
    print(solution.numberOfPairs(nums1, nums2, k))
