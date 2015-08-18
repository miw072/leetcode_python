# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(-10**10)
        dummy.next = head
        prev, curr = dummy, dummy.next
        while curr:
        	if curr.val == val:
        		prev.next = curr..next
        		curr = curr.next
        	else:
        		prev, curr = curr, curr.next

        return dummy.next			