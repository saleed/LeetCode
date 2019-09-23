# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        s=[ i+1 for i in range(n)]
        return self.dfs(s)


    def dfs(self,s):
        if len(s)==0:
            return [None]
        res=[]
        for i in range(len(s)):
            # root=TreeNode(s[i])
            leftArr=self.dfs(s[:i])
            rightArr=self.dfs(s[i+1:])
            for m in leftArr:
                for n in rightArr:
                    root=TreeNode(s[i])
                    root.left=m
                    root.right=n
                    res.append(root)
        return res


