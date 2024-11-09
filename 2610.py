from typing import List, Dict, Tuple

class Solution:
    def matrixRows(self, rows_dict: Dict[int, int]) -> Tuple[List[int], Dict[int, int]]:
        row = []
        new_dict = {}
        for key, value in rows_dict.items():
            row.append(key)
            if value > 1:
                new_dict[key] = value - 1
        return row, new_dict

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []
        rows_dict = {}
        
        for num in nums:
            if rows_dict.get(num):
                rows_dict[num] += 1 
            else:
                rows_dict[num] = 1

        qtd_rows = max(rows_dict.values())
        for _ in range(qtd_rows):
            row, rows_dict = self.matrixRows(rows_dict)
            matrix.append(row)
        return matrix
    
if __name__ == "__main__":
    access_solution = Solution()
    nums = [1,3,4,1,2,3,1]
    nums1 = [1,2,3,4]
    print(access_solution.findMatrix(nums1))
