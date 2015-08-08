class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
        	return 0
        profit = 0
        for i in xrange(1, len(prices)):
        	if prices[i] > prices[i-1]:
        		profit += prices[i] - prices[i-1]
        return profit			