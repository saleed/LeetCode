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
        res=[-float("inf")]
        self.dfs(root,res,None,0)
        return res[0]



    def dfs(self,root,res,parent,tmplen):
        if root==None:
            print(parent.val)
            res[0]=max(tmplen,res[0])
            return
        if parent==None or parent.val+1==root.val:
            self.dfs(root.left,res,root,tmplen+1)
            self.dfs(root.right,res,root,tmplen+1)
        else:
            res[0]=max(tmplen,res[0])
            self.dfs(root,res,None,0)




