# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0

        level=[[root,0]]
        maxl=0
        while len(level)>0:
            newlevel=[]
            maxl = max(maxl,level[-1][1]-level[0][1]+1)
            for p in range(len(level)):
                if level[p][0].left!=None:
                    newlevel.append([level[p][0].left,level[p][1]*2])
                if level[p][0].right!=None:
                    newlevel.append([level[p][0].right,level[p][1]*2+1])

            level=newlevel
        return maxl
