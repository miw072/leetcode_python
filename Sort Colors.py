class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        index = 0

        while index <= right:
        	if nums[index] == 0:
        		nums[index], nums[left] = nums[left], nums[index]
        		left+=1
        		index+=1
        	elif nums[index] == 2:
        		nums[index], nums[right] = nums[right], nums[index]
        		right-=1
        	else:
        		index+=1

        return			