"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        return self.constructSub(grid,0,len(grid)-1,0,len(grid[0])-1)


    def constructSub(self,grid,r1,r2,c1,c2):
        if r1<0 or r2<0 or r1>=len(grid) or r2>=len(grid) or c1<0 or c2<0 or c1>=len(grid[0]) or c2>=len(grid[0]):
            return None

        leafval= self.isLeaf(grid,r1,r2,c1,c2)
        if leafval!=-1:
             return Node(grid[r1][c1],True,None,None,None,None)

        ##default consider the len(grid) is always can be divided by 2

        tmpNode=Node(1,False,None,None,None,None)
        tmpNode.topLeft = self.constructSub(grid,r1,(r1+r2)/2,c1,(c1+c2)/2)
        tmpNode.topRight = self.constructSub(grid,r1,(r1+r2)/2,(c1+c2)/2+1,c2)
        tmpNode.bottomLeft = self.constructSub(grid,(r1+r2)/2+1,r2,c1,(c1+c2)/2)
        tmpNode.bottomRight = self.constructSub(grid,(r1+r2)/2+1,r2,(c1+c2)/2+1,c2)
        return tmpNode




    def isLeaf(self,grid,r1,r2,c1,c2):
        val=grid[r1][c1]
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                if grid[r][c]!=val:
                    return -1
        return val




