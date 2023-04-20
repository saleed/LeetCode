class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=l1
        q=l2
        newhead=ListNode(0)
        r=newhead
        c=0
        while p!=None or q!=None:
            pval=0 if p==None else p.val
            qval=0 if q==None else q.val
            addv=(pval+qval+c)
            r.next=ListNode(addv%10)
            c=addv/10
            p=p.next if p!=None else None
            q=q.next if q!=None else None
        if c:
            r.next=ListNode(c)
        return newhead.next