# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        _,_,isb=self.bst(root)

        return isb


    def bst(self,root):
        if root==None:
            return 0,0,True
        lmax,lmin,lisb=self.bst(root.left)
        rmax,rmin,risb=self.bst(root.right)
        return max(lmax,rmax)+1,min(lmin,rmin)+1,lisb and risb and abs(lmax-rmin)<=1 and abs(lmin-rmax)<=1