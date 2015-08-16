class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        appear, n = {}, len(nums)
        for i in nums:
        	appear[i] = i if i not in appear else appear[i] + 1
        for key in appear:
        	if appear[key] > n/2:
        		return key

        	