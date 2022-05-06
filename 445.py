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
        a=0
        while p!=None:
            a=a*10+p.val
            p=p.next
        p=l2
        b=0
        while p!=None:
            b=b*10+p.val
            p=p.next

        k=a+b
        res=ListNode(0)

        while k:

            new=ListNode(k%10)
            new.next=res.next
            res.next=new
            k=k/10
        return res


