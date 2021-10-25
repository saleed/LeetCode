# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
##任何一条路径，可以认为必须经过某一根节点，可以从上至下递归根节点
    以该根节点为跟的路径最大长度，为以左子节点为根的路径最大长度 +右子树的最大长度

"""
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[-float("inf")]
        self.recursive(root,res)
        return res[0]




    def recursive(self,root,res):
        if root==None:
            return 0
        llmax=self.recursive(root.left,res)
        rrmax=self.recursive(root.right,res)
        res[0]=max(res[0],root.val+max(llmax,0)+max(rrmax,0))
        return root.val+max(llmax,rrmax,0)


