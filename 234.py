# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return True
        if head.next==None:
            return True
        l=0
        p=head
        while p!=None:
            l+=1
            p=p.next
        p=head
        for _ in range(int(l/2)-1):
            p=p.next
        q=p.next
        p.next=None

        p=q
        q=p.next
        p.next=None
        if q!=None:
            r=q.next
        else:
            r=None
        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        q=head
        while q!=None and  p!=None:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next
        return True

