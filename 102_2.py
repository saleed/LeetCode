# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res=[]
        layer=[root]
        while len(layer)>0:
            vals=[]
            newlayer=[]
            for v in layer:
                vals.append(v.val)
                if v.left!=None:
                    newlayer.append(v.left)
                if v.right!=None:
                    newlayer.append(v.right)
            res.append(vals)
            layer=newlayer
        return res
