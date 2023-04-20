# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None

        maxid=0
        maxv=-float("inf")
        for i in range(len(nums)):
            if nums[i]>maxv:
                maxv=nums[i]
                maxid=i
        root=TreeNode(maxv)
        root.left=self.constructMaximumBinaryTree(nums[:maxid])
        root.right=self.constructMaximumBinaryTree(nums[maxid+1:])
        return root
