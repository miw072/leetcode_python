# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head or not head.next:
        	 return head

        dummy = ListNode(-10**4)
        dummy.next = head
        curr = head
        while curr.next:
        	if curr.val > curr.next.val:
        		pre, p = dummy, dummy.next
        		while p.val < curr.next.val:
        			pre, p = pre.next, p.next
        		tmp = curr.next
        		curr.next = tmp.next
        		tmp.next = p
        		pre.next = tmp
        	else:
        		curr = curr.next
        return dummy.next					 