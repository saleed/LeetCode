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
        if s=="":
            return [None]

        res=[]
        for i in range(len(s)):
            root=TreeNode(s[i])
            left=self.dfs(s[:i])
            right=self.dfs(s[i+1:])
            for l in range(len(left)):
                for r in range(len(right)):
                    root.left=left[l]
                    root.right=right[r]
                    res.append(copy.deepcopy(root))
        return res



