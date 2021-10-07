# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummyHead=ListNode(1)
        dummyHead.next=head
        p=dummyHead
        q=p.next
        r=None
        if q!=None:
            r=q.next
        while r!=None:
            p.next=r
            q.next=r.next
            r.next=q
            p=q
            q=p.next
            if q!=None:
                r=q.next
            else:
                r=None

        return dummyHead.next