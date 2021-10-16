# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        lrnode=self.flatten(root.left)
        rnode=self.flatten(root.right)
        if lrnode!=None:
            p=lrnode
            while p.right!=None:
                p=p.right
            p.right=rnode
            root.right=lrnode
            root.left=None
        return root

