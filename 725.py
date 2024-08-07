# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l=0
        p=head
        while p:
            l+=1
            p=p.next
        llist=[l/k]*k
        left=l%k
        for i in range(left):
            llist[i]+=1
        dum=ListNode(0)
        dum.next=head
        p=dum
        res=[]
        for l in llist:
            tmpl=0
            tmphead=p
            while p:
                tmpl+=1
                if tmpl==l-1:
                    res.append(tmphead)
                    q=p.next
                    p.next=None
                    p=q
                    break
                p = p.next
        return res

