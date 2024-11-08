class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_in_stones = {}
        qtd_jewels = 0

        for jewel in jewels:
            jewels_in_stones[jewel] = 1

        for possible_jewel in stones:
            if jewels_in_stones.get(possible_jewel):
                qtd_jewels += 1

        return qtd_jewels
    
if __name__ == "__main__":
    access_solution = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    jewels1 = "z"
    stones1 = "ZZ"
    print(access_solution.numJewelsInStones(jewels1, stones1))
