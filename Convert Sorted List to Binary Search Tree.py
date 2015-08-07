# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        self.q, n, p = head, 0, head
        while p:
        	p = p.next
        	n += 1
        return self.build(0, n-1)
        
    def build(self, start, end):
    	if start > end:
    		return None
    	mid = (start+end)/2
    	left = self.build(start, mid-1)
    	parent = TreeNode(self.q.val)
    	self.q = self.q.next
    	parent.left, parent.right = left, self.build(mid+1, end)
    	return parent	    	