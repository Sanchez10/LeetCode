from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            max_profit = max(max_profit, prices[i] - minimum)
        return max_profit
    
if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    prices1 = [7,6,4,3,1]
    print(s.maxProfit(prices))
