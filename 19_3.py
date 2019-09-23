# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        dummy=dummyhead

        count=1
        p=head
        while count<n and p!=None:
            p=p.next
            count+=1
        if p==None:
            return head
        while p.next!=None:
            p=p.next
            dummy=dummy.next

        q=dummy.next
        dummy.next=q.next
        q.next=None

        return dummyhead.next





