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
        dum=ListNode(0)
        dum.next=head
        p=dum
        q=p.next
        if q!=None:
            r=q.next
        else:
            return head
        while r!=None:
        
