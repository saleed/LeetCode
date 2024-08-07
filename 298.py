# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        self.dfs(root,res)
        return res[0]


    def dfs(self,root,res):
        if root==None:
            return 0

        lv=self.dfs(root.left,res)
        rv=self.dfs(root.right,res)

        len=1
        if root.left and root.left.val==root.val+1:
            len=max(len,lv+1)
        if root.right and root.right.val==root.val+1:
            len=max(len,rv+1)
        res[0]=max(res[0],len)
        return len







