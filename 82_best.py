# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy=ListNode(0)
        p=dummy
        dummy.next=head

        while p!=None:
            if p.next!=None and p.next.next!=None and p.next.val==p.next.next.val:
                q=p.next
                while q!=None and q.val==p.next.val:
                    q=q.next
                p.next=q
            else:
                p=p.next
        return dummy.next