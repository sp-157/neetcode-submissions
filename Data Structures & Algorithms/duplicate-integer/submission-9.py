class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = []
        for i in nums:
            if i in newArr:
                return True
            newArr.append(i)
        return False