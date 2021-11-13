"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
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

        p=head
        newhead=Node(0)
        q=newhead
        nodedict={}
        while p!=None:
            if p in nodedict:
                q.next=nodedict[p]
            else:
                q.next=Node(p.val)
                nodedict[p]=q.next
            q=q.next
            if p.random in nodedict:
                q.random=nodedict[p.random]
            elif  p.random!=None:
                q.random=Node(p.random.val)
                nodedict[p.random]=q.random
            p=p.next

        return newhead.next







