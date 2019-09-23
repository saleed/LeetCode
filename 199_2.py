# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        level=[root]
        res=[]

        while len(level)>0:
            nextlevel=[]
            for i in level:
                if i.left!=None:
                    nextlevel.append(i.left)
                if i.right!=None:
                    nextlevel.append(i.right)
            res.append(level[-1].val)
            level=nextlevel
        return res




