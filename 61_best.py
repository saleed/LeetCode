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
            return None
        tail=head
        l=1
        while tail.next!=None:
            l+=1
            tail=tail.next

        k=k%l
        p=head
        cnt=1
        while cnt<l-k:
            p=p.next
            cnt+=1
        q=p.next
        p.next=None
        tail.next=head
        return q
