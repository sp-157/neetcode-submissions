class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{', ')':'(', ']':'['}
        seen = []
        for i in s:
            if i not in brackets:
                seen.append(i)
            else:
                if not seen or seen[-1] != brackets[i]:
                    return False
                seen.pop()
        return not seen