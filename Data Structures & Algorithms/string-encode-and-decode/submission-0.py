class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + '|' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0

        while i < n:
            j = i
            while s[j] != '|':
                j += 1

            length = int(s[i:j])

            j += 1

            word = s[j:j+length]

            res.append(word)

            i = j+length

        return res



