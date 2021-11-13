# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head==None:
            return
        p=head
        q=None
        r=None
        if p!=None:
            q=p.next
        if q!=None:
            r=q.next
        p.next=None
        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
               r=r.next
        return p
