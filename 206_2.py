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
        q=head.next
        p.next=None ####注意这里如果无dummyhead要把头结点next先指空
        r=None
        if q!=None:
            r=q.next

        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next

        return p

