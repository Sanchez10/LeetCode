from typing import List

class Solution:
    def binary_search(self, row: List[int]) -> int:
        lenght_row = len(row)
        left, right = 0, lenght_row - 1
        first_negative_index = 0

        if row[0] < 0:
            return lenght_row
        elif row[lenght_row-1] >= 0:
            return 0

        while left <= right:
            middle = (left + right) // 2 
            if row[middle] < 0:
                if row[middle-1] > 0:
                    first_negative_index = middle
                    break
                else:
                    right = middle - 1
            elif row[middle] >= 0:
                if row[middle+1] < 0:
                    first_negative_index = middle + 1
                    break
                else:
                    left = middle + 1

        qtd_negative_row = lenght_row - first_negative_index
        return qtd_negative_row

    def countNegatives(self, grid: List[List[int]]) -> int:
        qtd_negative_numbers = 0
        for row in grid:
            qtd_negative_numbers += self.binary_search(row)
        return qtd_negative_numbers
    
if __name__ == "__main__":
    access_solution = Solution()
    matrix = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    matrix1 = [[3,2],[1,0]]
    print(access_solution.countNegatives(matrix))
