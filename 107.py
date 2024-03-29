# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        nodes=[root]
        res=[]
        while len(nodes)>0:
            val=[]
            newnodes=[]
            for n in nodes:
                val.append(n.val)
                if n.left!=None:
                    newnodes.append(n.left)
                if n.right!=None:
                    newnodes.append(n.right)
            res.append(val)
            nodes=newnodes
        return list(reversed(res))