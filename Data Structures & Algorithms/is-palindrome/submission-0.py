class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        if newS == newS[::-1]:
            return True
        return False