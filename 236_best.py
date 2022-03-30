# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root,p,q)




    def dfs(self,root,p,q):
        if root==p or root==q:
            return root
        lnode=self.dfs(root.left,p,q)
        rnode=self.dfs(root.right,p,q)
        if lnode!=None and rnode!=None:
            return root
        elif lnode!=None:
            return lnode
        elif rnode!=None:
            return rnode
        else:
            return None