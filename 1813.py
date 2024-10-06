
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1_split = sentence1.split(" ")
        s2_split = sentence2.split(" ")

        i, j = 0, 0
        
        while i < len(s1_split) and i < len(s2_split) and s1_split[i] == s2_split[i]:
            i += 1

        while j < len(s1_split) - i and j < len(s2_split) - i and s1_split[-1 - j] == s2_split[-1 - j]:
            j += 1

        return i + j == len(s1_split) or i + j == len(s2_split)

if __name__ == "__main__":
    access_solution = Solution()
    # sentence1 = "My name is Haley"
    # sentence2 = "My Haley"
    # sentence1 = "of"
    # sentence2 = "A lot of words"
    sentence1 = "Eating right now"
    sentence2 = "Eating"
    print(access_solution.areSentencesSimilar(sentence1, sentence2))
