# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        heightDict={}
        self.findLevel(root,heightDict)

        keys=heightDict.keys()
        keys.sort()
        res=[]
        for k in keys:
            res.append(heightDict[k])

        return res



    def findLevel(self,root,hegihtDict):
        if root==None:
            return 0
        left=self.findLevel(root.left,hegihtDict)
        right=self.findLevel(root.right,hegihtDict)
        height=min(left,right)+1
        if height in hegihtDict:
            hegihtDict[height].append(root.val)
        else:
            hegihtDict[height]=[root.val]



