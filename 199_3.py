# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#递归解法
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.dfs(res,root,1)
        return res


    def dfs(self,res,root,i):
        if root==None:
            return
        if len(res)<i:res.append(root.val)
        self.dfs(res,root.right,i+1)
        self.dfs(res,root.left,i+1)

