"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        maxd=0
        for c in root.children:
            d=self.maxDepth(c)
            maxd=max(maxd,d)
        return 1+maxd