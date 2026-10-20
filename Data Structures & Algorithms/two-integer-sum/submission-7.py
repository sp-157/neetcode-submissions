class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            newNum = target - num
            if newNum in numbers:
                return [numbers[newNum], i]
            numbers[num] = i
        return []
