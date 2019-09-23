# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head

        newhead=dummy

        while dummy.next!=None and dummy.next.next!=None:
            p=dummy.next
            q=p.next
            dummy.next=q
            p.next=q.next
            q.next=p
            dummy=p

        return newhead.next






