class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
        	return 0
        dp = [0 for i in xrange(len(nums)+1)]
        dp[0], dp[1] = 0, nums[0]
        for i in xrange(2, len(nums)+1):
        	dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[len(nums)]		