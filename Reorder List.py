# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head or not head.next: return

        p1, p2 = head, head.next
        while p2 and p2.next:
        	p1, p2 = p1.next, p2.next.next

        head2, p1.next = p1.next, None
        
        p2, head2.next = head2.next, None

        while p2:
        	p3 = p2.next
        	p2.next = head2
        	head2 = p2
        	p2 = p3

        p1, p2 = head, head2
        while p1:
        	t = p1.next
        	p1.next = p2
        	p1 = p1.next
        	p2 = t	

