# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False

        p=head
        q=head.next
        while p!=None and q!=None:
            if p==q:
                return True
            else:
                p=p.next
                q=q.next
                if q!=None:
                    q=q.next
                else:
                    return False
