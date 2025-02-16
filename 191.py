class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bit1 = 0
        while n > 0:
            if n & 1:
                n_bit1 += 1
            n >>= 1
        return n_bit1


if __name__ == "__main__":
    n = 11
    n1 = 128
    n2 = 2147483645
    s = Solution()
    print(s.hammingWeight(n2))
