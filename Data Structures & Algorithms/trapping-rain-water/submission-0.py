class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0]*n
        right_max = [0]*n

        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])

        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        area = 0
        for i in range(n):
            h = min(left_max[i], right_max[i])
            area += (h - height[i])

        return area


                