# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res,_=self.dfs(root)
        return res




    def dfs(self,root):
        if root==None:
            return 0,0
        lres,lsum=self.dfs(root.left)
        rres, rsum = self.dfs(root.right)
        return lres+rres+abs(lsum-rsum),lsum+rsum+root.val
