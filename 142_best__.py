# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head.next if head != None else None
        while q != None and p != q:
            if p != None and q.next != None:
                p = p.next
                q = q.next.next
            else:
                return None
        if q==None:
            return None
        print(p.val, q.val)
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p



head=ListNode(0)
p=head
for i in range(10):

