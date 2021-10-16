# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[float("inf")]
        if root==None:
            return 0
        self.dfs(root,res,1)
        return res[0]


    def dfs(self,root,res,cur):
        if root.left==None and root.right==None:
            res[0]=min(res[0],cur)
            return
        if root.left!=None:
            self.dfs(root.left,res,cur+1)
        if root.right!=None:
            self.dfs(root.right,res,cur+1)