# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        for j in range(len(inorder)):
            if preorder[0]==inorder[j]:
                root=TreeNode(preorder[0])
                root.left=self.buildTree(preorder[1:j+1],inorder[:j])
                root.right=self.buildTree(preorder[j+1:],inorder[j+1:])
        return root
