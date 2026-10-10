class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            newNum = target - nums[i]
            if newNum in dictionary:
                return [dictionary[newNum], i]
            dictionary[nums[i]] = i
