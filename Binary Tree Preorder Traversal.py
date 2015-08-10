# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root: return []
        res, stack = [], [root]
        while stack:
        	curr = stack.pop()
        	res.append(curr.val)
        	if curr.right: 
        		stack.append(curr.right)
        	if curr.left:
        		stack.append(curr.left)
        return res			