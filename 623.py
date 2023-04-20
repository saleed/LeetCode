# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth==1:
            newroot=TreeNode(val)
            newroot.left=root
            return newroot
        tmpnode=[root]
        d=2
        while d<depth:
            newnode=[]
            for v in  tmpnode:
                if v.left!=None:
                    newnode.append(v.left)
                if v.right!=None:
                    newnode.append(v.right)
            d+=1
            tmpnode=newnode
        for v in tmpnode:
            l=v.left
            r=v.right
            v.left=TreeNode(val)
            v.right=TreeNode(val)
            v.left.left=l
            v.right.right=r
        return root