class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        upper_dp = [None for k in xrange(len(triangle))]
        upper_dp[0] = triangle[0][0]
        dp = upper_dp[:]
        for row in triangle:
        	if len(row) == 1: continue
        	dp[0] = upper_dp[0] + row[0]
        	for i in xrange(1, len(row)-1):
        		dp[i] = row[i] + min(upper_dp[i], upper_dp[i-1])
        	dp[len(row)-1] = row[-1] + upper_dp[len(row)-2]
        	upper_dp = dp[:]
        return min(dp)		


