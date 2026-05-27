class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt_map = defaultdict(int)

        for num in nums:
            cnt_map[num] += 1

        freq = [[] for _ in range(n+1)]

        for num, cnt in cnt_map.items():
            freq[cnt].append(num)

        sz = len(freq)
        res = []
        length = 0

        for i in range(sz-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                length += 1

                if length == k:
                    return res
        