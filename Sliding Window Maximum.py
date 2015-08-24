class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0: return []
        queue = collections.deque(nums[:k])
        queue_max = max(queue)
        res = [queue_max]

        for i in xrange(k, len(nums)):
        	poped = queue.popleft()
        	queue.append(nums[i])
        	if nums[i] > queue_max: queue_max = nums[i]
        	elif poped == queue_max: queue_max = max(queue)
        	res.append(queue_max)

        return res
