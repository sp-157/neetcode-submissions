class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True