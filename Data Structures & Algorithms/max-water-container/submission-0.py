class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for l in range(n):
            for r in range(l+1, n):
                h = min(heights[l], heights[r])
                w = r - l

                max_area = max(max_area, h * w)
            

        return max_area