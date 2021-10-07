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
        p=l1
        q=l2
        c=0
        head=ListNode()
        r=head
        while p!=None or q!=None:
            pval=0
            qval=0
            if p!=None:
                pval=p.val
                p=p.next
            if q!=None:
                qval=q.val
                q=q.next
            newNode=ListNode()
            newNode.val=(pval+qval+c)%10
            c=(pval+qval+c)/10
            r.next=newNode
            r=r.next

        if c!=0:
            r.next=ListNode(1)

        return head.next



