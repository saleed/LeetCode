# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return head
        p=head
        l=0
        while p!=None:
            l+=1
            p=p.next

        mid=(l-1)/2
        p=head.next
        count=1
        while count<mid:
            p=p.next
            count += 1
        q=p.next
        while q!=None:
            t=q
            q=q.next
            t.next=p.next
            p.next=t
        sorthead=p.next
        self.printlinklist(head)
        p.next=None
        h=head
        q=sorthead
        # self.printlinklist(q)
        while h!=None and q!=None:
            t=q
            q=q.next
            t.next=h.next
            h.next=q
            h=t.next


    def printlinklist(self,head):
        while head!=None:
            print head.val
            head=head.next

