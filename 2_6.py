# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        r=head
        p=l1
        q=l2
        c=0
        while p!=None or q!=None:
            pval=0 if p is None else p.val
            qval=0 if q is None else q.val
            r.next=ListNode((pval+qval+c)%10)
            c=(pval+qval+c)/10
            p=p.next if p!=None else None
            q=q.next if q!=None else None
            r=r.next
        if c:
            r.next=ListNode(c))
            
        return head.next
