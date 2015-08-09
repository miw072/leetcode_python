	# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.maxSum = -10 ** 10
        self.findMax(root)
        return self.maxSum

    def findMax(self, node):
    	if not node: return 0
    	l = self.findMax(node.left)
    	r = self.findMax(node.right)
    	self.maxSum = max(self.maxSum, l + node.val + r)
    	ret = node.val + max(l, r)
    	return ret if ret >0 else 0