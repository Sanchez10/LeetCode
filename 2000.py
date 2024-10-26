
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index = word.find(ch)
        prefix = word[:index]
        sufix = word[index:]
        return sufix[0] + prefix[::-1] + sufix[1:]

if __name__ == "__main__":
    access_solution = Solution()
    word = "abcdefd"
    ch = "d"
    word1 = "xyxzxe"
    ch1 = "z"
    word2 = "abcd"
    ch2 = "z"
    print(access_solution.reversePrefix(word1, ch1))
