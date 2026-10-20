class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = set()
        for i in nums:
            if i in newArr:
                return True
            newArr.add(i)
        return False