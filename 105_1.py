# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder)==len(inorder)==0:
            return None
        root=TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                root.left=self.buildTree(preorder[1:i+1],inorder[:i])
                root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
                break
        return root