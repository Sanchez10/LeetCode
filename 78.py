from typing import List

class Solution:   
    def backtrack(self, response: List[List[int]], temp: List[int], nums: List[int], start: int) -> List[List[int]]:
        response.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(response, temp, nums, i + 1)
            temp.pop()
        return response

    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []
        self.backtrack(response, [], nums, 0)
        return response
    
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    nums1 = [0]
    print(s.subsets(nums1)) 
