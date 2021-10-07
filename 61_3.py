# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head

        dummy=ListNode(0)
        dummy.next=head
        tail=head
        l=1

        while tail.next!=None:
            tail=tail.next
            l+=1
        i=0
        p=dummy

        while i<l-k:
            p=p.next
            i+=1
        newhead=p.next
        p.next=None
        tail.next=head
        return newhead






    def reverseList(self,head):
        if head==None:
            return None
        if head.next==None:
            return head

        p=head
        q=head.next
        r=q.next
        head.next=None
        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        return p
