# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dumhead=ListNode()
        dumhead.next=head

        count=0
        p=head
        while p!=None and count<n:
            count+=1
            p=p.next

        if count<n:
            return dumhead.next

        q=dumhead
        while p!=None:
            p=p.next
            q=q.next


        dn=q.next
        q.next=q.next.next
        dn.next=None
        return dumhead.next


