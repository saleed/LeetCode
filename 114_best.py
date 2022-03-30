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
        l_flat=self.flatten(root.left)
        r_flat=self.flatten(root.right)
        root.left=None
        root.right=l_flat
        p=root

        while p.right!=None:
            p=p.right
        p.right=r_flat
        return root


