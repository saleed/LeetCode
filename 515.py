# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeN   ode
        :rtype: List[int]
        """

        level=[root]
        res=[]
        while len(level)>0:
            maxv=-float("inf")
            newlevel=[]
            for v in level:
                if v.val>maxv:
                    maxv=v.val
                if v.left!=None:
                    newlevel.append(v.left)
                if v.right!=None:
                    newlevel.append(v.right)
            res.append(maxv)
            level=newlevel
        return res
