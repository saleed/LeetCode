# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        if head.next.next==None:
            p=head
            q=head.next
            q.next=p
            p.next=None
            return q
        p1=head
        p2=head.next
        p3=head.next.next
        p1.next=None
        while p3!=None:
            p2.next=p1
            p1=p2
            p2=p3
            p3=p3.next
        p2.next=p1
        return p2

