# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        l=self.getheight(root.left)
        r=self.getheight(root.right)
        if abs(r-l)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def getheight(self,root):
        if root==None:
            return 0
        return 1+max(self.getheight(root.left),self.getheight(root.right))

