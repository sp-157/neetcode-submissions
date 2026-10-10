class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []
        if len(s) < 2:
            return False
        for char in s:
            if char in brackets:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                if opener != brackets[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True