# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None


        l=ListNode(0)
        p=head
        while p!=None:
            q=l
            while q.next!=None and q.next.val<p.val :
                q=q.next

            np=p.next
            p.next=q.next
            q.next=p
            p=np
        return l.next

