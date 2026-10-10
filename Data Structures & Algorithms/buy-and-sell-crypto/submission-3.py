class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        profit = prices[1] - prices[0]

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                check = prices[j] - prices[i]
                if check > profit:
                    profit = check
        if profit < 0:
            profit = 0
        return profit
                