# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        while root:
        	if root.left:
        		p = root.left
        		while p.right: p = p.right
        		p.right = root.right
        		root.right = root.left
        		root.left = None
        	root = root.right	