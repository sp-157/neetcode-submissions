class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for charS,charT in zip(s, t):
            countS[charS] = 1 + countS.get(charS, 0)
            countT[charT] = 1 + countT.get(charT, 0)
        return countS == countT