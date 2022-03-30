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
        nodedict={}

        return self.recursive(head,nodedict)



    def recursive(self,head,nodedict):
        if head==None:
            return None

        if head not in nodedict:
            newhead=Node(head.val)
            nodedict[head]=newhead
            newhead.next=self.recursive(head.next,nodedict)
            newhead.random=self.recursive(head.random,nodedict)
            return newhead
        else:
            return nodedict[head]



