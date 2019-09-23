# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        dummy=p

        dummy.next=head

        while dummy.next!=None:
            if dummy.next.val==val:
                dummy.next=dummy.next.next
            else:
                dummy=dummy.next
        return p.next