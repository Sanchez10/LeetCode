class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sort_points = sorted(points)
        difference_between_x = 0
        j = 1
        for i in range(len(sort_points) - 1):
            difference_sides = sort_points[j][0] - sort_points[i][0]
            if difference_between_x <= difference_sides:
                difference_between_x = difference_sides
            j += 1
        return difference_between_x


if __name__ == "__main__":
    s = Solution()
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    points1 = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    print(s.maxWidthOfVerticalArea(points1))
