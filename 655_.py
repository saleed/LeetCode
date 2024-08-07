# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        nlist=[]

        tmp=[(root,0,0)]
        maxh=0
        h=0
        while len(tmp)>0:
            nlist.extend(tmp)
            ntmp=[]
            for v in tmp:
                h=v[1]
                c=v[2]
                if v.left:
                    ntmp.append((v.left,h+1,c-pow(2,c-))

