"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.recursive(root)
        return root



    def recursive(self,root):
        if root==None:
            return
        p=root
        prenode=None
        firstNode=None
        while p!=None:
            if p.left!=None:
                if prenode!=None:
                    prenode.next=p.left
                prenode=p.left
            if p.right!=None:
                if prenode!=None:
                    prenode.next=p.right
                prenode=p.right
            if firstNode==None:
                firstNode=p.left if p.left!=None else p.right
            p=p.next

        self.recursive(firstNode)
