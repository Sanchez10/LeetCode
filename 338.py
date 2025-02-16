from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            i_bin = bin(i)[2:]
            i_bin = i_bin.replace("0", "")
            ans.append(len(i_bin))
        return ans


if __name__ == "__main__":
    n = 2
    n1 = 5
    s = Solution()
    print(s.countBits(n1))
