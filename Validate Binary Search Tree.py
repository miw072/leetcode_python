# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
    	self.prev = None
    	return self.isIncreasing(root)

    def isIncreasing(self, p):
    	if not p:return True
    	if self.isIncreasing(p.left):
    		if self.prev and self.prev.val >= p.val :return False
    		self.prev = p
    		return self.isIncreasing(p.right)
    	return False		