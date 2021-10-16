# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """


        if len(inorder)==len(postorder)==0:
            return None
        root=TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i]==postorder[-1]:
                root.left=self.buildTree(inorder[:i],postorder[:i])
                root.right=self.buildTree(inorder[i+1:],postorder[i:-1])
                break
        return root