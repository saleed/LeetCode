# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        dummy=ListNode(float("inf"))
        dummy.next=head
        p=dummy
        q=head
        while q!=None:
            if q.val!=p.val:
                p.next=q
                p=q
                q=q.next
                p.next=None
            else:
                q=q.next
        return dummy.next




