# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        res=[]
        if root==None:
            return res
        self.dfs(root,[],0,res,targetSum)


    def dfs(self,node,cur,cur_sum,res,target):
        if node.left==None and node.right==None and cur_sum+node.val==target:
            cur.append(node.val)
            res.append(cur[:])
            return

        if node.left!=None:
            res.append(node.val)
            self.dfs(node.left,cur,cur_sum+node.val,res,target)
            res.pop()

        if node.right!=None:
            res.append(node.val)
            self.dfs(node.right,cur,cur_sum+node.val,res,target)
            res.pop()





