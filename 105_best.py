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

        root=preorder[0]
        index=0
        for i in range(len(inorder)):
            if inorder[i]==root:
                index=i
                break

        rootNode=TreeNode()
        rootNode.val=root
        rootNode.left=self.buildTree(preorder[1:1+index],inorder[:index])
        rootNode.right=self.buildTree(preorder[1+index:],inorder[index+1:])
        return rootNode