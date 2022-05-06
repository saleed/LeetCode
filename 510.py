"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node.right==None:
            if node.parent!=None and node.parent.val>node.val:
                return node.parent
            else:
                p=node.parent
                while p!=None and p.val<=node.val:
                    p=p.parent
                return p
        else:
            p=node.right
            while p.left!=None:
                p=p.left
            return p
