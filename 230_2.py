# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


##不是最优解法，计算节点数量可以和dfs的过程合二为一

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return -1
        leftNum=self.NodeNum(root.left)
        if leftNum==k-1:
            return root.val
        elif leftNum>k-1:
            return self.kthSmallest(root.left,k)
        else:
            return self.kthSmallest(root.right,k-leftNum+1)






    def NodeNum(self,root):
        if root==None:
            return 0
        return 1+self.NodeNum(root.left)+self.NodeNum(root.right)
