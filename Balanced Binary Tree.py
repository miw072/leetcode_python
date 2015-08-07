# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, node):
    	if not node: return 0
    	l = self.maxDepth(node.left)
    	if l == -1: return -1
    	r = self.maxDepth(node.right)
    	if r == -1: return -1
    	return max(l,r)+1 if abs(l-r)<=1 else -1