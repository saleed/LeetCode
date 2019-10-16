# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        return self.find(0,root)





    def find(self,flag,node):
        if node==None:
            return 0
        if flag==1:
            if node.left==None and node.right==None:
                return node.valqqq

        return self.find(1,node.left)+self.find(0,node.right)





a=Solution()
a.sumOfLeftLeaves()
