# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
        	return False
        if not (root.left or root.right):
        	return root.val == sum
		res = False
		if root.left:
			res =  self.hasPathSum(root.left, sum - root.val)		
		if root.right:
			res =  res or self.hasPathSum(root.right, sum - root.val)
		return res				

