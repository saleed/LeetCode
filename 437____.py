# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root==None:
            return 0
        res=[0]
        self.dfs(root,targetSum,float("inf"),res)
        return res[0]



    def dfs(self,root,targetsum,preval,res):
        if root==None:
            return
        if preval+root.val==targetsum:
            res[0]+=1

        self.dfs(root.left,targetsum,0,res)
        self.dfs(root.right,targetsum,0,res)

        self.dfs(root.left, targetsum, root.val, res)
        self.dfs(root.right, targetsum, root.val, res)
        if preval!=float("inf"):
            self.dfs(root.left,targetsum,root.val+preval,res)
            self.dfs(root.right,targetsum,root.val+preval,res)


