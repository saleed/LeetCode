"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        head,tail=self.recursive(head)
        return head


    def recursive(self,head):
        if head==None:
            return None,None
        p=head
        prePtr=None
        while p!=None:
            prePtr=p
            if p.child!=None:
                chead,ctail=self.recursive(p.child)
                ctail.next=p.next
                if p.next!=None:
                    p.next.prev=ctail
                p.next=chead
                chead.prev=p
                p.child=None
                p=ctail.next
            else:
                p=p.next

        return head,prePtr