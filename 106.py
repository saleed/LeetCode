# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        for j in range(len(inorder)):
            if postorder[-1]==inorder[j]:
                root=TreeNode(postorder[-1])
                root.left=self.buildTree(inorder[:j],postorder[:j])
                root.right=self.buildTree(inorder[j+1:],postorder[j:-1])
        return root