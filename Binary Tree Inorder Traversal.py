# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        cur, res, stack = root, [], []
        while stack or cur:
        	while cur:
        		stack.append(cur)
        		cur = cur.left
        	poped = stack.pop()
        	res.append(poped.val)
        	cur = poped.right
        return res		