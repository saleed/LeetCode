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
        dummyhead=ListNode(0)
        r=dummyhead
        while p!=None or q!=None:

            pval=float("inf") if p==None else p.val
            qval=float("inf") if q==None else q.val
            select=None
            if pval<qval:
                select=p
                p=p.next
            else:
                select=q
                q=q.next
            select.next=None
            r.next=select
        return dummyhead.next
