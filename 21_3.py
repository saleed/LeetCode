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
            if pval<qval:
                p=p.next
                r.next=ListNode(pval)
                r=r.next
            else:
                q=q.next
                r.next=ListNode(qval)
                r=r.next
        return dummyhead.next