# Remove Duplicates from Sorted Array II 
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	if len(nums) <= 2:
    		return len(nums)
    	counter, fast = 1, 1
    	for fast in xrange(1, len(nums)):
    		counter = counter + 1 if nums[fast] == nums[fast-1] else 1
    		if counter < 2:
    			continue
    		nums[slow] = nums[fast]
    		slow+=1
    	return slow		 	