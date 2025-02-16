class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            x ^= num
        for i in range(len(nums) + 1):
            x ^= i
        return x


if __name__ == "__main__":
    s = Solution()
    nums = [3, 0, 1]
    nums1 = [0, 1]
    nums2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s.missingNumber(nums))
