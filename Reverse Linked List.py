# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        newHead = None
        while head:
        	nextNode = head.next
        	head.next = newHead
        	newHead = head
        	head = nextNode
        return newHead	