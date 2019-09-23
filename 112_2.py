# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # if root==None:
        #     return False
        # return self.dfs(root,sum)

        return self.dfs1(root,sum)

    def dfs(self,root,sum):
        if root==None and sum==0:
            return True
        elif root!=None:
            return (self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val))  #这种方法是错误的！！！
        else:
            return False



    def dfs1(self,root,sum):
        if root==None:
            return False
        if root.val==sum and root.left==None and root.right==None:
            return True
        return self.dfs1(root.left,sum-root.val) or self.dfs1(root.right,sum-root.val)

