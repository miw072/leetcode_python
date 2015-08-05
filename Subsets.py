class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        self.result, self.nums, self.n = [], nums, len(nums)
        self.dfs([], 0, self.n)
        return self.result

    def dfs(self, L, start, len):
    	self.result.append(L)
    	for i in xrange(start, len):
    		self.dfs(L+[self.nums[i]], i+1, self.n)    