
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 12:42
# @Author  : sunaolin
# @File    : 572_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root==None or subRoot==None:
            return False
        if root.val==subRoot.val and self.compareSub(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def compareSub(self,root1,root2):
        if root1==None or root2==None:
            return True
        if root1.val==root2.val:
            return self.compareSub(root1.left,root2.left) and self.compareSub(root1.right,root2.right)
        else:
            return False