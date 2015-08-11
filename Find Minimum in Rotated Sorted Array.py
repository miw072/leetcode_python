class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        L, R = 0, len(nums)-1
        Min = nums[0]
        while L < R-1:
        	M = L + (R - L)/2
        	if (nums[L] < nums[M]):
        		Min = min(Min, nums[L])
        		L = M + 1
        	else:
        		Min = min(Min, nums[M])
        		R = M - 1
        Min = min(nums[R], Min)
        Min = min(nums[L], Min)		
        return Min			
