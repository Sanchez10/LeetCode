class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        letter_position_s = {}
        letter_position_t = {}
        permutation_difference = 0

        for i, caracter in enumerate(s):
            letter_position_s[caracter] = i

        for i, caracter in enumerate(t):
            letter_position_t[caracter] = i
        
        for key, value in letter_position_s.items():
            permutation_difference += abs(value - letter_position_t.get(key))

        return permutation_difference
    
if __name__ == "__main__":
    access_solution = Solution()
    s = "abc"
    t = "bac"
    s1 = "abcde"
    t1 = "edbac"
    print(access_solution.findPermutationDifference(s1, t1))
