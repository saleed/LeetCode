# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res,_,_=self.dfs(root)
        return res

    def dfs(self,root):
        if root==None:
            return 0,0,0 ##最大长度， 跟节点为起始点 递增递减
        lasc=1
        rasc=1
        ldesc=1
        rdesc=1
        lmaxl,leftasc,leftdesc=self.dfs(root.left)
        rmaxl,rightasc,rightdesc=self.dfs(root.right)
        if root.left!=None:
            if root.val==root.left.val+1:
                lasc=leftasc+1
            elif root.val==root.left.val-1:
                ldesc=leftdesc+1
        if root.right!=None:
            if root.val==root.right.val+1:
                rasc=rightasc+1
            elif root.val==root.right.val-1:
                rdesc=rightdesc+1

        return max(lmaxl,rmaxl,ldesc+rasc-1,lasc+rdesc-1),max(lasc,rasc),max(ldesc,rdesc)


