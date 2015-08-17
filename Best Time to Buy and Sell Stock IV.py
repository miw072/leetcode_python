class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if k <= len(prices)/2:
        	dp = [None for i in xrange(2*k+1)]
        	dp[0] = 0
        	for i in xrange(len(prices)):
        		for j in xrange(1, min(2*k+1, i +2)):
        			dp[j] = max(dp[j], dp[j-1]+prices[i] * [1, -1][j % 2])
        	return max(dp)
        else:
        	sum = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    sum += prices[i] - prices[i - 1]
            return sum			