# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #转成数字，然后相加，再转成链表
        d1=self.linkListToDigit(l1)
        d2=self.linkListToDigit(l2)
        return self.digitToLinkList(d1+d2)




    def linkListToDigit(self,head):
        if head==None:
            return 0
        p=head
        res=0
        mul=1
        while p!=None:
            res+=p.val*mul
            mul*=10
            p=p.next
        return res
    def digitToLinkList(self,digit):
        if digit<0:
            return None
        if digit==0:
            return ListNode(0)
        dummyHead=ListNode(-1)
        pre=dummyHead

        while digit>0:
            p=digit%10
            digit/=10
            pre.next=ListNode(p)
            pre=pre.next
        return dummyHead.next


