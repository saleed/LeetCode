# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        while True:
            left=self.NodeNum(root.left)
            if left+1==k:
                return root.val
            elif left+1<k:
                return self.kthSmallest(root.right,k-left-1)
            else:
                return self.kthSmallest(root.left,k)




    def NodeNum(self,root):
        if root==None:
            return 0
        else:
            return 1+self.NodeNum(root.left)+self.NodeNum(root.right)