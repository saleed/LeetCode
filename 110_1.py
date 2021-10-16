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
        bst,_=self.dfs(root)
        return bst


    def dfs(self,root):
        if root==None:
            return True,0
        lbst,lh=self.isBalanced(root.left)
        rbst,rh=self.isBalanced(root.right)
        return lbst and rbst and abs(lh-rh)<=1,max(lh,rh)
