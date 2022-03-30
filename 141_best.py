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
        if head == None:
            return False

        p = head
        q = head.next
        while p != None:
            if p == q:
                return True
            if q != None and q.next != None:
                q = q.next.next
            else:
                return False
            p = p.next