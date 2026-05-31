class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        s_set = set()
        l = 0
        max_len = 0

        for r in range(n):
            while l < r and s[r] in s_set:
                s_set.remove(s[l])
                l += 1

            s_set.add(s[r])
            max_len = max(max_len, r-l+1)

        return max_len


        

