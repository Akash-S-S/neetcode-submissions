class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        if ns != nt:
            return False

        cnt_map = defaultdict(int)
        for i in range(ns):
            cnt_map[s[i]] += 1
            cnt_map[t[i]] -= 1

        for ch in cnt_map:
            if cnt_map[ch] != 0:
                return False

        return True