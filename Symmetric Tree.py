# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True
        return self.check(root.left, root.right)

    def check(self, l, r):
    	if not (l or r): return True
    	if not (l and r): return False
    	if l.val != r.val: return False
    	return self.check(l.left, r.right) and self.check(l.right, r.left)    


    	###########################################

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        # thanks to https://leetcode.com/discuss/26372/python-iterative-way-using-a-queue
        if not root: return True
        Q = collections.deque([root.left, root.right])
        while Q:
            node1, node2 = Q.popleft(), Q.popleft()
            if not (node1 or node2): continue # both None
            if not (node1 and node2): return False
            if node1.val != node2.val: return False
            Q.append(node1.left)
            Q.append(node2.right)
            Q.append(node1.right)
            Q.append(node2.left)
        return True