# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        dummy1, dummy2 = ListNode(0), ListNode(0)
        p1, p2 = dummy1, dummy2
        while head:
        	if head.val < x:
        		p1.next = head
        		p1 = p1.next
        	else:
        		p2.next = head
        		p2 = p2.next
        	head = head.next
        p1.next, p2.next = dummy2.next, None
        return dummy1.next			