# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushMostLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.stack else False

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        if node.right:
        	self.pushMostLeft(node.right)
        return node.val
        
    def pushMostLeft(self, curr):
    	while curr:
    		self.stack.append(curr)
    		curr = curr.left    	


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())