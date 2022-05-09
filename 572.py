# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if self.compare(root,subRoot):
            return True
        if root!=None and (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)):
            return True
        return False

    def compare(self,r1,r2):
        if r1==None and r2==None:
            return True
        if r1!=None and r2!=None:
            return r1.val==r2.val and self.compare(r1.left,r2.left) and self.compare(r1.right,r2.right)
        return False



