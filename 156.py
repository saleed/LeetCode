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
        la=self.getLen(headA)
        lb=self.getLen(headB)
        if la>lb:
            longh=headA
            shorth=headB
        else:
            longh=headB
            shorth=headA
        count=1
        p=longh
        while count<=abs(la-lb):
            p=p.next
            count+=1
        q=shorth
        self.printlsit(p)
        self.printlsit(q)
        while p!=None:
            if p==q:  #has no attribulte val
                return p
            p=p.next
            q=q.next
        return None




    def getLen(self,head):
        l=0
        p=head
        while p!=None:
            l+=1
            p=p.next
        return l
    def printlsit(self,head):
        p=head
        res=[]
        while p!=None:
            res.append(p)
            p=p.next
        return res
    