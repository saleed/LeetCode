# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """


        _,node=self.dfs(root,k)
        return node


    def dfs(self,root,k):
        if root==None:
            return 0,None
        leftnum,node=self.dfs(root.left,k)
        if node!=None:
            return leftnum,node
        if leftnum==k-1:
            return leftnum,root
        rightnum,node=self.dfs(root.right,k-leftnum-1)
        return leftnum+rightnum,node





