# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        tmp = [root]
        flag=True
        while len(tmp) > 0:
            ntmp = []
            tmpres = []
            for p in tmp:
                tmpres.append(p.val)
                if p.left:
                    ntmp.append(p.left)
                if p.right:
                    ntmp.append(p.right)
            tmp = ntmp
            if flag:
                res.append(tmpres)
            else:
                res.append(tmpres[::-1])
            flag= not flag
        return res
