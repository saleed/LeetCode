# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """


        if root==None:
            return ""
        left=self.tree2str(root.left)
        right=self.tree2str(root.right)
        res=str(root.val)
        if len(right)>0:
            res+="("+left+")"
            res+="("+right+")"
        elif len(left)>0:
            res+="("+left+")"
        return res