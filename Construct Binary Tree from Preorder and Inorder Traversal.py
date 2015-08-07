# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        self.p, self.i = preorder, inorder
        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1)

    def dfs(self, l1, r1, l2, r2):
    	if l1 > r1:
    		return None
    	if l1 == r1:
    		return TreeNode(self.p[l1])

    	root, pos = TreeNode(self.p[l1]), self.i.index(self.p[l1])
    	root.left = self.dfs(l1+1, l1+pos-l2, l2, pos-1)
    	root.right = self.dfs(l1+pos-l2+1, r1, pos+1, r2)

    	return root		    