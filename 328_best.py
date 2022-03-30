# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        dum=ListNode(0)
        dum.next=head
        cnt=0
        odlist=ListNode(0)
        p=dum
        q=odlist
        while p.next!=None:
            if cnt%2==1:
                r=p.next.next
                q.next=p.next
                q=q.next
                q.next=None
                p.next=r
            else:
                p=p.next
            cnt+=1
        p.next=odlist.next
        return dum.next





