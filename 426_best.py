"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        lmin,rmax=self.recursive(root,None)
        return lmin


    def recursive(self,root,father):
        if root==None:
            return None,None
        lmin,lmax=self.recursive(root.left,root)
        rmin,rmax=self.recursive(root.right,root)

        if rmin != None:
            root.right=rmin
        elif father!=None and father.val>root.val:
            root.right=father
        else:
            root.right=None
        if lmax!=None:
            root.left=lmax
        elif father!=None and father.val<root.val:
            root.left=father
        else:
            root.left=None

        leftmin=root
        if lmin!=None:
            leftmin=lmin
        elif lmax!=None:
            leftmin=lmax

        rightmax=root
        if rmax!=None:
            rightmax=rmax
        elif rmin!=None:
            rightmax=rmin
        return leftmin,rightmax












