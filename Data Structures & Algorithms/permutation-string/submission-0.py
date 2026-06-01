class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        cnt1, cnt2 = [0]*26, [0]*26

        for i in range(n1):
            idx = ord(s1[i]) - ord('a')
            cnt1[idx] += 1

        l, r = 0, 0

        for r in range(n2):
            idx = ord(s2[r]) - ord('a')
            cnt2[idx] += 1

            while (r - l + 1) > n1:
                idx = ord(s2[l]) - ord('a')
                cnt2[idx] -= 1
                l += 1

            if cnt1 == cnt2:
                return True

        return False