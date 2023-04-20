# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return None

        l=0
        p=head
        while p!=None:
            l+=1
            p=p.next
        i=0
        dum=ListNode(0)
        dum.next=head
        p=dum
        while i<l-n: ###倒数第n个，是正数第l-n+1个数，但是如果从0开始标记，则为第l-n个标记数
            p=p.next
        q=p.next
        p.next=q.next
        q.next=None
        return dum.next
