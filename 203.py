# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        q=dummy
        while q.next!=None:
            if q.next.val==val:
                p=dummy.next
                q.next=p.next
                p.next==None
            else:
                q=q.next
        return dummy.next