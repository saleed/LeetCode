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

        target=preorder[0]
        id=-1
        for i in range(len(inorder)):
            if inorder[i]==target:
                id=i
        root=TreeNode(int(target))
        root.left=self.buildTree(preorder[1:1+id],inorder[:id])
        root.right=self.buildTree(preorder[1+id:],inorder[id+1:])
        return root





