# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        return max(self.dfs(0,root.left)+self.dfs(0,root.right),root.val+self.dfs(1,root.left)+self.dfs(1,root.right))

    ##超时!!!!!!!!

    def dfs(self,flag,root):
        if root==None:
            return 0
        lrob0=self.dfs(0,root.left)
        rrob0=self.dfs(0,root.right)

        lrob1=self.dfs(1,root.left)
        rrob1=self.dfs(1,root.right)
        if flag==1:
            return lrob0+rrob0
        else:
            return max(rrob0+lrob0,root.val+lrob1+rrob1)


