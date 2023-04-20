# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root==None:
            return -1
        if root.left==None and root.right==None:
            return -1
        if root.left.val==root.val==root.right.val:
            left=self.findSecondMinimumValue(root.left)
            right=self.findSecondMinimumValue(root.right)
            if left==-1 and right==-1:
                return -1
            elif left==-1:
                return right
            elif right==-1:
                return left
            else:
                return min(left,right)
        elif root.left.val==root.val:
            left = self.findSecondMinimumValue(root.left)
            if left==-1:
                return root.right.val
            else:
                return min(left,root.right.val)
        else:
            right = self.findSecondMinimumValue(root.left)
            if right == -1:
                return root.left.val
            else:
                return min(right, root.left.val)