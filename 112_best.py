# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root==None:
            return False

        return self.dfs(root,targetSum,0)


    def dfs(self,node,target,tmpsum):
        if node==None:
            return False
        elif node!=None:
            if node.left == None and node.right == None and tmpsum + node.val == target:
                return True
            return self.dfs(node.left,target,tmpsum+node.val) or self.dfs(node.right,target,tmpsum+node.val)
        else:
            return False
