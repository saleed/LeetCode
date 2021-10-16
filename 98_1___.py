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
        a,b,ret=self.dfs(root)
        return ret


    def dfs(self,root):
        if root==None:
            return -float("inf"),float("inf"),True
        lmax,lmin,lbst=self.dfs(root.left)
        rmax,rmin,rbst=self.dfs(root.right)



        return max(rmax,root.val),min(root.val,lmin),lbst and rbst and root.val>lmax and root.val<rmin

