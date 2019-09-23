# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _,_,ret=self.recursive(root)
        if ret:
            return True
        else:
            return False

    #出错！！！

    # 执行出错信息：
    # Line
    # 25: TypeError: 'bool'
    # object is not iterable
    # 最后执行的输入：
    # [2, 1, 3
    def recursive(self,root):
        if root==None:
            return -float("inf"), float("inf"), True
        lmax,lmin,lbst=self.isValidBST(root.left)
        rmax,rmin,rbst=self.isValidBST(root.right)
        if root.val>lmax and root.val<rmin and lbst and rbst:
            return max(root.val, rmax), min(root.val, lmax), True
        else:
            return float("inf"), float("inf"), False


