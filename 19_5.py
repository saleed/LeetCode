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

        l=0
        p=head
        while p!=None:
            p=p.next
            l+=1
        if l<n:
            return head
        cnt=l-n
        dummyhead=ListNode(0)
        dummyhead.next=head
        i=0
        p=dummyhead
        while i<cnt:
            p=p.next
            i+=1

        if p!=None and p.next!=None:
            q=p.next
            p.next=q.next
            q.next=None

        return dummyhead.next
