class Solution:
    def isValid(self, s: str) -> bool:
        # brackets = {'{': '}', '[':']', '(':')'}
        brackets = {'}': '{', ']':'[', ')':'('}
        seen = []
        for i in s:
            if i in brackets:
                if not seen or seen[-1] != brackets[i]:
                    return False
                seen.pop()
            else:
                seen.append(i)

            # if i in brackets:
            #     if seen:
            #         if i != brackets[seen.pop()]:
            #             return False
            # seen.append(i)
        return not seen


        