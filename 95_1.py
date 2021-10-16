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

        res=self.dfs(node)
        return res



    def dfs(self,nodes):
        if len(nodes)==0:
            return [None]

        res=[]
        for i in range(len(nodes)):
            lTrees=self.dfs(nodes[:i])
            rTrees=self.dfs(nodes[i+1:])
            for l in lTrees:
                for r in rTrees:
                    root=TreeNode(nodes[i])
                    root.left=l
                    root.right=r
                    res.append(root)
        return res






