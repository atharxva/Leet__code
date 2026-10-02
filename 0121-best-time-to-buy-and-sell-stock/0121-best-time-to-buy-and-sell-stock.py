class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0

        for price in prices:
            min_price = min(price , min_price)
            profit = price - min_price
            max_price = max(profit , max_price)
        return max_price