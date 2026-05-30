class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1

        max_area = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l

            max_area = max(max_area, h * w)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return max_area
        