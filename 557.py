class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        reverse_list = []
        for word in s_list:
            reverse_list.append(word[::-1])
        reverse_string = " ".join(reverse_list)
        return reverse_string
        
if __name__ == "__main__":
    access_solution = Solution()
    s = "Let's take LeetCode contest"
    s1 = "Mr Ding"
    print(s)
    access_solution.reverseWords(s)
