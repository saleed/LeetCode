# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        p=root
        n=self.getLeftNodeNum(p.left)+1
        base=0
        while base+n!=k:
            print base,n
            if base+n<k:
                base+=n
                p=p.right
            else:
                p=p.left
            if p==None:
                return -1
            n=self.getLeftNodeNum(p.left)+1

        return p.val


    def getLeftNodeNum(self,root):
        if root==None:
            return 0
        else:
            return self.getLeftNodeNum(root.left)+self.getLeftNodeNum(root.right)+1

