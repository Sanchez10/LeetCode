from typing import List

class Solution:
    def removeNthFromEnd(self, head: List[int], n: int) -> List[int]:
        head.remove(head[-n])
        return head

if __name__ == "__main__":
    access_solution = Solution()
    head = [1,2]
    n = 1
    print(access_solution.removeNthFromEnd(head, n))
