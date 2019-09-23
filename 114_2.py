# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        q=root.right
        p=self.flatten(root.left)
        root.right=p
        p=root
        while p.next:
            p=p.next
        p.next=self.flatten(q)
        return root
