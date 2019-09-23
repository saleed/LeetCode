# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None

        l=self.getLen(head)
        if k%l==0:
            return head
        k=l-k%l
        p=head
        count=1
        while count<k:
            p=p.next
            count+=1
        q=p.next
        p.next=None
        newhead=q
        while q.next!=None:
            q=q.next
        q.next=head
        return newhead



    def getLen(self,head):
        p = head
        n = 0
        while p != None:
            p = p.next
            n = n + 1
        return n