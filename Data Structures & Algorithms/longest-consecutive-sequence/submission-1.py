class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums_set = set(nums)

        max_consec_cnt = 1

        for num in nums_set:
            if num-1 not in nums_set:
                curr_num = num
                consec_cnt = 1

                while curr_num + 1 in nums_set:
                    consec_cnt += 1
                    curr_num += 1

                max_consec_cnt = max(max_consec_cnt, consec_cnt)

        return max_consec_cnt

