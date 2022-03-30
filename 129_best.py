# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        self.dfs(root,res,0)
        return res[0]

    def dfs(self,root,res,tmp):
        if root==None:
            return
        if root.left==None and root.right==None:
            res[0]+=tmp
            return
        self.dfs(root.left,res,tmp*10+root.val)
        self.dfs(root.right,res,tmp*10+root.val)
