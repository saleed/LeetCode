# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        sumset=set()
        lrootsum=self.check(sumset,root.left)
        rrootsum=self.check(sumset,root.right)
        rootsum=root.val+lrootsum+rrootsum  ###防止rootsum为0的情况

        if rootsum%2==0 and rootsum/2 in sumset :
            return True
        return False

    def check(self,sumset,root):
        if root==None:
            return 0
        left=self.check(sumset,root.left)
        right=self.check(sumset,root.right)

        tmpsum=left+right+root.val


        sumset.add(tmpsum)
        return tmpsum
