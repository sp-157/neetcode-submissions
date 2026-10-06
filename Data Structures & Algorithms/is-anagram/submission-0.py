class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            st = "".join(sorted(s))
            ts = "".join(sorted(t))
            if st == ts:
                return True
        return False