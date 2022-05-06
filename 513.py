# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        level=[root]
        while len(level)>0:
            res=level[0]
            newlevel=[]
            for n in level:
                if n.left!=None:
                    newlevel.append(n.left)
                if n.right!=None:
                    newlevel.append(n.right)
            level=newlevel
        return res
