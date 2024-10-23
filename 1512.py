from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # pair_of_number = {}
        qtd_good_pairs = 0
        for i in range(len(nums)):
            # print(f"i: {i}, num[i]: {nums[i]}")
            for j in range(i+1, len(nums)):
                # print(f"j: {j}, num[j]: {nums[j]}")
                if nums[i] == nums[j]:
                    if i < j:
                        qtd_good_pairs += 1
        return qtd_good_pairs
    
if __name__ == "__main__":
    access_solution = Solution()
    test = [1,2,3,1,1,3]
    test2 = [1,1,1,1]
    test3 = [1,2,3]
    print(access_solution.numIdenticalPairs(test3))
