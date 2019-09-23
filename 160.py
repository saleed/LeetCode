# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la=self.getlen(headA)
        lb=self.getlen(headB)
        if la<lb:
            for i in range(lb-la):
                headB=headB.next
        else:
            for i in range(la-lb):
                headA=headA.next
        while headA!=None:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next





    def getlen(self,head):
        count=0
        p=head
        while p!=None:
            count+=1
            p=p.next
        return count
