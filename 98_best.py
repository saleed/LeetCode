# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        vmax,vmin,isv=self.recursive(root)
        return isv


    def recursive(self,root):
        if root==None:
            return -float("inf"),float("inf"),True
        lmax,lmin,lisv=self.recursive(root.left)
        rmax,rmin,risv=self.recursive(root.right)
        return max(root.val,lmax,rmax),min(lmin,root.val,rmin),lisv and risv and lmax<root.val<rmin