# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        self.inorder(root,res)
        minv=float("inf")
        for i in range(1,len(res)):
            minv=min(minv,res[i]-res[i-1])
        return minv


    
    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

