# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.dfs(root)



        
    def dfs(self,root):
        if root==None:
            return 0
        else:
            if self.findvalue(root,root.val):
                return 1+self.findvalue(root.left)+self.findvalue(root.right)
            else:
                return self.findvalue(root.left)+self.findvalue(root.right)


    def findvalue(self,root,val):
        if root==None:
            return True
        else:
            return root.val==val and self.findvalue(root.left,val) and self.findvalue(root.right,val)