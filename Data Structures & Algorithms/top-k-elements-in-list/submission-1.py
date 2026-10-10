class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        pairs = []
        for num,cnt in count.items():
            pairs.append([cnt,num])
        pairs.sort()
        result = []
        while len(result) < k:
            result.append(pairs.pop()[1])
        return result