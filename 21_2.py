# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p=l1
        q=l2
        newhead=ListNode(0)
        r=newhead
        while p!=None or q!=None:
            pval=float("inf")
            qval=float("inf")
            if p!=None:
                pval=p.val
            if q!=None:
                qval=q.val
            if pval<qval:
                p=p.next
                r.next=ListNode(pval)
            else:
                q=q.next
                r.next=ListNode(qval)
        return newhead.next



