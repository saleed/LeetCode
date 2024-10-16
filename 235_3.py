# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


###多余搜索
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==p or root==q:
            return root
        else:
            lnum=self.findNum(root.left,p,q)
            if lnum==2:
                return self.lowestCommonAncestor(root.left,p,q)
            elif lnum==1:
                return root
            else:
                return self.lowestCommonAncestor(root.right,p,q)




    def findNum(self,root,p,q):
        if root==None:
            return 0
        if root==p or root==q:
            return 1+self.findNum(root.left,p,q)+self.findNum(root.right,p,q)
        else:
            return self.findNum(root.left,p,q)+self.findNum(root.right,p,q)

