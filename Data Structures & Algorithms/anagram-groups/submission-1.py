class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            abc = [0] * 26
            for char in i:
                abc[ord(char) - ord('a')] += 1
            key = tuple(abc)
            if key not in res:
                res[key] = []
            res[key].append(i)
        return list(res.values())
