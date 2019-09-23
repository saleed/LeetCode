"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None

        dict={}
        dummy=Node(0,head,None)
        dummy.next=head
        copydummy=Node(0,None,None)
        p=dummy
        q=copydummy
        while p!=None:
            if p.next!=None:
                if p.next in dict.keys():
                    q.next=dict[p.next]
                else:
                    q.next=Node(p.next.val,None,None)
                    dict[p.next]=q.next
            if  p.random !=None:
                if p.random in dict.keys():
                    q.random=dict[p.random]
                else:
                    q.random=Node(p.random.val,None,None)
                    dict[p.random]=q.random
            p=p.next
            q=q.next
        return copydummy.next


