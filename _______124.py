# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.val
        return max(self.maxSumWithRoot(root),self.maxSumWithRoot(root.left),self.maxSumWithRoot(root.right))


    def maxSumWithRoot(self,root):
        if root==None:
            return 0
        return max(0,self.maxPathSum(root.left)+self.maxPathSum(root.right)+root.val)
