class Solution:
    def how_many_zeros_and_ones(self, substring: str, k: int) -> int:
        zeros = 0
        ones = 0
        for number in substring:
            if number == '0':
                zeros += 1
            elif number == '1':
                ones += 1

        if zeros <= k or ones <= k:
            return 1
        else:
            print(substring)
            return 0

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        qtd_substrings = 0
        for idx in range(len(s)):
            for idx2 in range(idx, len(s)):
                qtd_substrings += self.how_many_zeros_and_ones(s[idx:idx2+1], k)
        return qtd_substrings

if __name__ == "__main__":
    access_solution = Solution()
    s = "10101"
    k = 1
    s1 = "1010101"
    k1 = 2
    s2 = "11111"
    k2 = 1
    print(access_solution.countKConstraintSubstrings(s1, k1))
