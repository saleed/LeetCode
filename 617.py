# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root1,root2)



    def dfs(self,root1,root2):
        if root1==None and root2==None:
            return None
        v1=0
        v2=0
        r1left=None
        r1right=None
        r2left=None
        r2right=None
        if root1!=None:
            v1=root1.val
            r1left=root1.left
            r1right=root1.right
        if root2!=None:
            v2=root2.val
            r2left=root2.left
            r2right=root2.right
        root=TreeNode(v1+v2)
        root.left=self.dfs(r1left,r2left)
        root.right=self.dfs(r1right,r2right)
        return root