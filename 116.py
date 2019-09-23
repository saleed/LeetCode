"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
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
        level=[root]
        while len(level)>0:
            level.append(None)
            newlevel=[]
            for i in range(len(level)-1):
                level[i].next=level[i+1]
                if level[i].left!=None:
                    newlevel.append(level[i].left)
                if level[i].right!=None:
                    newlevel.append(level[i].right)
            level=newlevel
        return root



