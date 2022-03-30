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
        num,_=self.dfs(root)
        return num




    def dfs(self,root):
        if root==None:
            return 0,float("inf")
        if (root.left==None and root.right==None):
            return 1,root.val

        l,lv=self.dfs(root.left)
        r,rv=self.dfs(root.right)

        if (root.left!=None and root.right!=None and lv==rv==root.val) or\
                (root.left==None and rv==root.val) or\
                (root.right==None and lv==root.val):
            return l+r+1,root.val
        else:
            return l+r,float("inf")