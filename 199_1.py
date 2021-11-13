# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        node=[root]
        res=[]
        while len(node)>0:
            res.append(node[-1].val)
            newnode=[]
            for v in node:
                if v.left!=None:
                    newnode.append(v.left)
                if v.right!=None:
                    newnode.append(v.right)
            node=newnode

        return res
