# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        res=[0]
        self.dfs(root,res)
        return res[0]


    def dfs(self,root,res):
        if root==None:
            return float("inf"),-float("inf"),True,0
        lmin,lmax,lisbst,lnum=self.dfs(root.left,res)
        rmin,rmax,risbst,rnum=self.dfs(root.right,res)
        if lisbst and risbst and root.val>lmax and root.val<rmin:
            if res[0]<lnum+rnum+1:
                res[0]=lnum+rnum+1
            return min(root.val,lmin),max(root.val,rmax),True,lnum+rnum+1
        return float("inf"),-float("inf"),False,0
