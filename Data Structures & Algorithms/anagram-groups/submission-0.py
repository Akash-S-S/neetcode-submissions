class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)

        for s in strs:
            cnt = [0]*26

            for ch in s:
                cnt[ord(ch) - ord('a')] += 1

            mpp[tuple(cnt)].append(s)

        return list(mpp.values())