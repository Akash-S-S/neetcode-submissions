class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        if nt > ns:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        
        required = len(need)
        formed = 0

        l = 0
        min_len = float('inf')
        start = 0

        for r in range(ns):
            ch = s[r]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    start = l

                left_ch = s[l]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                l += 1

        return "" if min_len == float('inf') else s[start: start+min_len]




        



        