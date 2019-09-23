# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next=head


        pre=float("inf")

        p=dummy

        while p.next!=None:
            count=0
            pre=p.next.val
            q=p.next
            while q!=None and q.val==pre:
                count+=1
                q=q.next
            if count==1:
                p=p.next
            elif count>=2:
                p.next=q
        return dummy.next


