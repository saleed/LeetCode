# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lhead=ListNode(0)
        rhead=ListNode(0)

        r=lhead
        s=rhead

        p=head
        while p!=None:
            q=p.next
            if p.val<x:
                r.next=p
                r=r.next
            else:
                s.next=p
                s=s.next
            p.next=None
            p=q

        if lhead.next==None:
            return rhead.next
        else:
            r.next=rhead.next
            return lhead.next