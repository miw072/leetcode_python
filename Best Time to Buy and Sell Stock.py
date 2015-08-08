class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0
        minPrice, diff = 10**10, -10**10
        for price in prices:
        	minPrice = min(minPrice, price)
        	diff = max(diff, price - minPrice)
        return diff	