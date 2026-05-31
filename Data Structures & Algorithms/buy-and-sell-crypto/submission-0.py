class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]   # Fix 3
        max_profit = 0

        for price in prices:    # Fix 1
            if price < min_price:
                min_price = price   # Fix 2

            profit = price - min_price      # Fix 4
            max_profit = max(max_profit, profit)

        return max_profit