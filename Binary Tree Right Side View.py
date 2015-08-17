# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root: return []
        D = {}
        Q = collections.deque([(root, 1)])

        while Q:
        	curr = Q.popleft()
        	D[curr[1]] = curr[0].val
        	if curr[0].left: Q.append((curr[0].left, curr[1]+1))
        	if curr[0].right: Q.append((curr[0].right, curr[1]+1))
        return [D[key] for key in sorted(D.keys())]	