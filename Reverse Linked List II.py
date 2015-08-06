# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in xrange(m-1): pre = pre.next
        start, then = pre.next, pre.next.next

        for i in xrange(n-m):
        	start.next = then.next
        	then.next = pre.next
        	pre.next = then 
        	then = start.next

        return dummy.next	
