# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """


        dummy=ListNode(0)
        dummy.next=head
        count=1
        p=dummy
        while count<m:
            p=p.next
            count+=1
        save=p
        p=p.next
        if p==None or p.next==None:
            return p
        q=p.next
        # p.next=None
        r=q.next
        while count<n:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        tail=save.next
        save.next=p
        tail.next=q
        return dummy.next


