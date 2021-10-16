# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res=[]
        layer=[root]
        flag=1
        while len(layer)>0:
            vals=[]
            newlayer=[]
            for v in layer:
                vals.append(v.val)
                if v.left!=None:
                    newlayer.append(v.left)
                if v.right!=None:
                    newlayer.append(v.right)
            if flag>0:
                res.append(vals)
            else:
                res.append(vals[::-1])
            layer=newlayer
            flag=-flag
        return res