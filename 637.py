# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if root==None:
            return 0
        nodelist=[root]
        res=[]
        while True:
            newlist=[]
            tmpsum=0
            for r in nodelist:
                tmpsum+=r.val
                if r.left!=None:
                    newlist.append(r.left)
                if r.right!=None:
                    newlist.append(r.right)
            res.append(float(tmpsum)/float(len(nodelist)))
            if len(newlist)==0:
                return res
            else:
                nodelist=newlist


