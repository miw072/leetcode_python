# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr:
        	nextLevelFirst, prev = None, None
        	while curr:
        		if not nextLevelFirst: nextLevelFirst = curr.left if curr.left else curr.right
        		if curr.left: 
        			if prev: prev.next = curr.left
        			prev = curr.left
        		if curr.right: 
        			if prev: prev.next = curr.right
        			prev = curr.right
        		curr = curr.next
        	curr = nextLevelFirst			