# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp={}
        self.robDfs(root,dp,0)
        return dp[root]


    def robDfs(self,root,dp,pre):
        if root==None:
            return 0
        else:
            dpval=[]
            if root in dp:
                dpval=dp[root]
            else:
                dp[root]=[0]*2
                dp[root][0]=self.robDfs(root.left,dp,0)+self.robDfs(root.right,dp,0)
                dp[root][1]=self.robDfs(root.left,dp,1)+self.robDfs(root.rgiht,dp,1)+root.val
            if pre == 0:
                return max(dpval)
            else:
                return dpval[0]
