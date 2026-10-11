class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        for i in range(len(nums)):
            newNum = target - nums[i]
            if newNum in numIndex:
                return [numIndex[newNum], i]
            numIndex[nums[i]] = i
        return []