class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            countS[i] = 1+countS.get(i, 0)
            countT[j] = 1+countT.get(j, 0)
        
        return countS == countT