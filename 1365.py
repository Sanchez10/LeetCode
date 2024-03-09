from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        qtd_of_smaller_numbers = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            qtd_of_smaller_numbers.append(count)
        return qtd_of_smaller_numbers

if __name__ == "__main__":
    nums = [1,5,7,23,9,6,8,0]
    access_solution = Solution()
    print(access_solution.smallerNumbersThanCurrent(nums))
