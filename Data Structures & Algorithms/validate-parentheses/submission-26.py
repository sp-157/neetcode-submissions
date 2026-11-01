class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        new = []
        for i in s:
            if i in brackets:
                if not new or new[-1] != brackets[i]:
                    return False
                new.pop()
            else:
                new.append(i)
        return not new