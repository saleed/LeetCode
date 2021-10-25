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



    def recursive(self,root):
        if root==None:
            return
        nextrnode=None
        if root.left!=None:
            root.left.next=root.right
        if root.right!=None:
            nextrnode=root.right
        nextlnode=None
        if root.next!=None:
            nextlnode=root.next.left if root.next.left!=None else root.next.right
        if nextrnode!=None:
            nextrnode.next=nextlnode
        self.recursive(root.left)
        self.recursive(root.right)
