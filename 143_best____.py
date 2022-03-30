# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        l1=ListNode(0)
        l2=ListNode(0)



        cnt=0
        p=head
        q=l1
        r=l2
        while p!=None:
            if cnt%2==0:
                q.next=p
                q=p
                p=p.next
                q.next=None
            else:
                np=p.next
                p.next=r.next
                r.next=p
                p=np

        dummyhead = ListNode(0)
        p=dummyhead
        q=l1.next
        r=l2.next

        while q!=None or r!=None:
            if q!=None:
                p.next=q
                q=q.next
            if r!=None
                p.next=r
                r=r.next
            p=p.next

        return dummyhead.next
