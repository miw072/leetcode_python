class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 10**10
        for i in xrange(len(nums)-2):
        	left = i + 1
        	right = len(nums) - 1
        	while left < right:
        		closestSum = nums[i] + nums[left] + nums[right]
        		if closestSum == target:
        			return closestSum
        		elif closestSum < target:
        			left += 1
        		else:
        			right -= 1
        		closest = closestSum if abs(closest-target) > abs(closestSum-target) else closest			

        return closest			