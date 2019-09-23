# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        val=self.dfs(root)
        return max(val[0],val[1])




    ###使用双返回值,减少了搜索次数
    def dfs(self,root):
        if root==None:
            return 0,0
        right=self.dfs(root.right)
        left=self.dfs(root.left)
        return max(left[0],left[1])+max(right[0],right[1]),root.val+left[0]+right[0]


