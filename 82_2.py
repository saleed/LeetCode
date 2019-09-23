# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p!=None:
            if p.next==None:
                return dummy.next
            elif p.next.next==None:
                return dummy.next
            elif p.next.val==p.next.next.val:
                q=p.next
                while q!=None and q.val==p.next.val:
                    q=q.next
                p.next=q

            elif p.next.val!=p.next.next.val:
                p=p.next

