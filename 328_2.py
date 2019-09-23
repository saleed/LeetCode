# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head

        dummy1=ListNode(0)
        dummy2=ListNode(0)
        dummy1.next=dummy2
        dummy2.next=head
        p=dummy1
        q=dummy2
        while p!=None and q!=None: