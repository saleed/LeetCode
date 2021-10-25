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

        if head==None:
            return
        l=0
        p=head
        while p!=None:
            l+=1
            head=head.next

        cnt=1
        p=head
        while cnt<l/2:
            p=p.next
            cnt+=1
        q=None

        if p!=None:
            q=p.next
        r=None
        if q!=None:
            r=q.next
        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        tail=p



