class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            newNum = target - n
            if newNum in hashmap:
                return [hashmap[newNum], i]
            hashmap[n] = i
                