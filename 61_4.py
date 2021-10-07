# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None
        l=0
        p=head
        tail=None
        while p!=None:
            l+=1
            tail=p
            p=p.next

        offset=l-k%l
        dummyhead=ListNode(0)
        dummyhead.next=head
        p=dummyhead
        cnt=0
        while cnt<offset:
            p=p.next
            cnt+=1

        tail.next=dummyhead.next
        dummyhead.next=p.next
        p.next=None
        return dummyhead.next