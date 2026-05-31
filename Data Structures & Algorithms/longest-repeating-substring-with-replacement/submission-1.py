class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        cnt_map = defaultdict(int)
        res = 0

        l = 0
        max_cnt = 0

        for r in range(n):
            cnt_map[s[r]] += 1
            max_cnt = max(max_cnt, cnt_map[s[r]])

            while (r-l+1) - max_cnt > k:
                cnt_map[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
            