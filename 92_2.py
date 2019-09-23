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

        count=0
        p=dummy
        while count<m-1:
            p=p.next
            count+=1
        count=0
        q=dummy
        while count<n:
            q=q.next
            count+=1
        s=p.next
        e=q
        save=e.next
        s,e=self.reverse(s,e)
        p.next=s
        e.next=save

        return dummy.next






    def reverse(self,s,e):
        if s==e:
            return s,s
        if s.next==e:
            e.next=s
            s.next=None
            return e,s
        p=s
        q=s.next
        r=s.next.next
        s.next=None
        while p!=e:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        return e,s





