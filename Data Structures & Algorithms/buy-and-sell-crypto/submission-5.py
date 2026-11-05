class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]
        for i in prices:
            if i < price:
                price = i
            diff = i - price
            if diff > profit:
                profit = diff
        return profit