# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return
        tmp=root.right
        root.right=root.left
        root.left=tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
