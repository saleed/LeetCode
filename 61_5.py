# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        l=0
        p=head
        while p:
            l+=1
            p=p.next
        k=k%l
        if k==0:
            return head
        cnt=1
        p=head
        while cnt<l-k:
            p=p.next
            cnt+=1
        q=p.next
        p.next=None
        p=q
        while p.next:
            p=p.next
        p.next=head
        return q