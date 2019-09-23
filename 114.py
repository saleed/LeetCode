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
        else:
            q=root.right
            root.right=self.flatten(root.left)
            root.left=None
            ptr=root
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=self.flatten(root.right)
            return root
