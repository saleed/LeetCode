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
        lr=None
        rl=None
        if root.left!=None:
            root.left.next=root.right
            lr=root.left
        if root.right!=None:
            lr=root.right
        if root.next!=None:
            if root.next.left!=None:
                rl=root.next.left
            elif root.next.right!=None:
                rl=root.next.right
        if lr is not None:
            lr.next=rl
        self.recursive(root.left)
        self.recursive(root.right)

