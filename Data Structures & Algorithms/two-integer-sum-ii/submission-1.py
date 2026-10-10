class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        add = numbers[left] + numbers[right]
        while left < right:
            if add == target:
                return [left+1, right+1]
            add = numbers[left] + numbers[right]            
            if add < target:
                left += 1
            if add > target:
                right -=1
        return []