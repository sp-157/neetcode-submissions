class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            if price < minimum:
                minimum = price
            profit = price - minimum
            if profit > maximum:
                maximum = profit

        return maximum