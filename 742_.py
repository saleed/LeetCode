# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return None
        res=[TreeNode(float("inf"))]
        self.dfs(root,k,res)
        return res[0].val


    def dfs(self,root,k,res):
        print(res[0].val)
        if root.left==None and root.right==None and abs(res[0].val-k)>abs(root.val-k):
            res[0]=root
        if root.left:
            self.dfs(root.left,k,res)
        if root.right:
            self.dfs(root.right,k,res)

