# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs1(root,sum,[],res)
        return res



    def dfs1(self,root,sum,cur,res):

        #//这样写是错误的！！！！
        # if root==None:
        #     if 0==sum:
        #         res.append(cur[:])
        #     return

        if root==None:
            return
        if root.val==sum and root.left==None and root.right==None:  ##########这里的判断是关键！！！
            # return True
            cur.append(root.val)
            res.append(cur[:])
            cur.pop()

        cur.append(root.val)
        self.dfs1(root.left,sum-root.val,cur,res)
        self.dfs1(root.right,sum-root.val,cur,res)
        cur.pop()

