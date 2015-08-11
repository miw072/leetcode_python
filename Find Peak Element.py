class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        left, right = 0, len(num)-1
        while left + 1 < right:
        	mid = left + (left - right)/2
        	if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
        		return mid
        	elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
        		left = mid
        	else:
        		right = mid
		return left if nums[left] > nums[right] else right			