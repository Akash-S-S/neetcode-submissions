class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        new_s = []

        for ch in s:
            if ch.isalnum():
                new_s.append(ch.lower())

        n = len(new_s)
        l, r = 0, n-1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1

        return True