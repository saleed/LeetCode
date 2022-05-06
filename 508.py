# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sumdict={}
        self.dfs(root,sumdict)
        maxv=-float("inf")
        for k in sumdict:
            if maxv<sumdict[k]:
                maxv=sumdict[k]
        res=[]
        for k in sumdict:
            if sumdict[k]==maxv:
                res.append(k)
        return res



    def dfs(self,root,sumdict):
        if root==None:
            return 0
        lsum=self.dfs(root.left,sumdict)
        rsum=self.dfs(root.right,sumdict)
        sumv=lsum+rsum+root.val
        if lsum+rsum in sumdict:
            sumdict[sumv]+=1
        else:
            sumdict[sumv]=1
        return lsum+rsum

