# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p = list1
        q = list2
        new = ListNode(0)
        r = new
        while p != None or q != None:
            pval = p.val if p != None else float("inf")
            qval = q.val if q != None else float("inf")
            if pval < qval:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
            r.next = None
        return new.next
