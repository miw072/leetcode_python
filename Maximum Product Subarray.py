class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        Max, fk, gk = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
        	fk, gk = max(fk * nums[i], gk * nums[i], nums[i]), min(fk * nums[i], gk * nums[i], nums[i])
        	Max = max(fk, Max)
        return Max	 