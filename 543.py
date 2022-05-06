# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodenum,_=self.dfs(root)
        return nodenum-1


    def dfs(self,root):
        if root==None:
            return 0,0,0
        l,lmax=self.diameterOfBinaryTree(root.left)
        r,rmax=self.diameterOfBinaryTree(root.right)

        return max(l,r,lmax+rmax+1),max(lmax,rmax)+1

