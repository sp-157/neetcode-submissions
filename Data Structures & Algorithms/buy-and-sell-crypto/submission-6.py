class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]
        for i in prices:
            if i < price:
                price = i
            if profit < (i - price):
                profit = i - price
        return profit