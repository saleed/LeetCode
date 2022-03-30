# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        p=head
        q=p.next
        r=q.next if q!=None else None
        p.next=None
        while q!=None:
            q.next=p
            p=q
            q=r
            r=r.next if r!=None else None
        return p