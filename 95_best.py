# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        node=[i for i in range(1,n+1)]

        return self.recursive(node)



    def recursive(self,node):
        if len(node)==0:
            return [None]
        res=[]
        for i in range(len(node)):
            lres=self.recursive(node[:i])
            rres=self.recursive(node[i+1:])
            for l in lres:
                for r in rres:
                    root=TreeNode(node[i])
                    root.left=l
                    root.right=r
                    res.append(root)
        return res
