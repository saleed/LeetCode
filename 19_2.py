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
        dummyhead=ListNode(0)
        dummyhead.next=head
        ll=0
        p=head
        while ll<n and p!=None:
            p=p.next
            ll+=1
        if p==None and ll<n:  ######这个条件没想清楚
            return None
        new=dummyhead
        while p!=None:
            new=new.next
            p=p.next
        q=new.next
        new.next=q.next
        q.next=None
        return dummyhead.next


