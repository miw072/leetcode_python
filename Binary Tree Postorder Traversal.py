# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root: return []
        res, stack, previous = [], [root], 'Initial'
        while stack:
        	top = stack[-1]
        	if (not top.left and not top.right) or previous in (top.left, top.right):
        		res.append(top.val)
        		previous = top
        		stack.pop()
        	else:
        		if top.right:
        			stack.append(top.right)
        		if top.left:
        			stack.append(top.left)
        return res					