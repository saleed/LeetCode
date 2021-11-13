# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        newhead,_=self.quickSort(head)
        return newhead




    def quickSort(self,head):
        if head==None:
            return None,None
        print(head)
        lhead,rhead,base=self.findbase(head)
        nlhead,nltail=self.quickSort(lhead)
        nrhead,nrtail=self.quickSort(rhead)
        l=None
        r=None
        if lhead==None:
            l=base
        else:
            l=nlhead
        if rhead==None:
            r=base
        else:
            r=nrtail
        if nltail!=None:
            nltail.next=base
        base.next=nrhead

        return l,r


    def findbase(self,head):
        if head==None:
            return None,None,None
        base=head
        p=head.next
        base.next=None
        lList=ListNode(0)
        rList=ListNode(0)
        lp=lList
        rp=rList
        while p!=None:
            if p.val<base.val:
                lp.next=p
                lp=lp.next
            else:
                rp.next=p
                rp=rp.next

            np = p.next
            p.next = None
            p=np
        return lList.next,rList.next,base


