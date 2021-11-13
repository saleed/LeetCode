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

        l = 0
        p = head
        while p != None:
            l += 1
            p = p.next

        p = head
        cnt = 0
        while cnt < l / 2:
            cnt += 1
            p = p.next
        q = p.next
        p.next = None

        p = q
        q = None
        if p != None:
            q = p.next
            p.next = None  ###improtant####################notic
        r = None
        if q != None:
            r = q.next

        while q != None:
            q.next = p
            p = q
            q = r
            if r != None:
                r = r.next

        # print(p)
        q = p
        p = head

        while p != None and q != None:
            np = p.next
            nq = q.next
            p.next = q
            q.next = np
            p = np
            q = nq

        return head






