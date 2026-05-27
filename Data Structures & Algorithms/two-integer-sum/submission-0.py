class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        prev_map = {}

        for i in range(n):
            diff = target - nums[i]
            if diff in prev_map:
                return [prev_map[diff], i]

            else:
                prev_map[nums[i]] = i

        return [-1, -1]