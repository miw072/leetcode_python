# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        self.res = []
        self.preOrder(root, 0)
        return self.res

    def preOrder(self, node, depth):
    	if not node: return
    	if len(self.res) == depth: self.res.insert(0,[])
    	self.res[-depth-1].append(node.val)
    	self.preOrder(node.left, depth+1)
    	self.preOrder(node.right, depth+1)