class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
    	nums.sort()
        self.result, self.nums, self.n = [], nums, len(nums)
        self.dfs([], 0, self.n)
        return self.result

    def dfs(self, L, start, len):
    	self.result.append(L)
    	for i in xrange(start, len):
    		if i != start and self.nums[i] == self.nums[i-1]:
    			continue
    		self.dfs(L+[self.nums[i]], i+1, self.n)