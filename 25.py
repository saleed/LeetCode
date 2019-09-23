# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p=head
        newhead=head
        flag=0
        curhead=head
        while True:
            count=1
            while count<k and p!=None:
                p=p.next
                count+=1
            #只有count==k and p!=None的时候才能继续，否则返回None
            if count<k:
                return newhead
            if p==None:
                return newhead
            curtail=p
            nexthead=p.next
            p.next=None
            if flag==0:
                newhead=curtail
                flag=1
            self.reverseLinkList(curhead)
            curhead.next = nexthead
            curhead=nexthead
            p=nexthead


    def reverseLinkList(self,head):
        if head==None or head.next==None:
            return
        p=head
        q=head.next
        r=head.next.next
        p.next = None
        while q!=None:
            q.next=p
            p=q
            q=r
            if r!=None:
                r=r.next
        newhead=p
        return newhead

