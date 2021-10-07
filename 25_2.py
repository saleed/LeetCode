# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyhead=ListNode(0)
        dummyhead.next=head
        p=dummyhead
        q=None
        while p!=None:
            cnt=0






    def reverse(self,head,tail):
        if head==None:
            return head

        p=head.next
        q=p.next if p!=None else None
        r=q.next if q!=None else None
        while q!=tail:
            q.next=p
            p=q
            q=r
            if r!=None
                r=r.next
            else:
                r=None
        if head.next!=None:
            head.next.next=tail
        head.next=p

