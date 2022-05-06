# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        nlist=[]
        p=head
        while p!=None:
            nlist.append(p)
            p=p.next
        c=(nlist[-1].val+1)/10
        nlist[-1].val=(nlist[-1].val+1)%10
        for i in range(len(nlist)-1)[::-1]:
            nv=(nlist[i].val+c)%10
            c=(nlist[i].val+c)/10
            nlist[i].val=nv
        if c>0:
            newhead=ListNode(1)
            newhead.next=head
            return newhead
        else:
            return head


