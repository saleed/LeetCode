
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if len(grid)==0 or len(grid[0])==0:
            return None

        return self.constructQuad(grid,0,0,len(grid))




    def constructQuad(self,grid,tlx,tly,width):
        state=self.isLeaf(grid,tlx,tly,width)
        if state==0:
            return Node(True,True,None,None,None,None)
        elif state==1:
            return Node(False,True,None,None,None,None)
        else:
            res=Node(None,None,None,None,None,None)
            res.isLeaf=False
            res.val=True
            res.topLeft=self.constructQuad(grid,tlx,tly,int(width/2))
            res.topRight=self.constructQuad(grid,tlx,int(tly+width/2),int(width/2))
            res.bottomLeft=self.constructQuad(grid,int(tlx+width/2),tly,int(width/2))
            res.bottomRight=self.constructQuad(grid,tlx,int(tly+width/2),int(width/2))

            return res






    def isLeaf(self,grid,tlx,tly,width):
        count=0
        for i in range(tlx,tlx+width):
            for j in range(tly,tly+width):
                if grid[i][j]==0:
                    count+=1



        if count==0:
            return 0
        elif count==width*width:
            return 1
        else:
            return 2

a=Solution()


grid= [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
a.construct(grid)

"""


{"$id":"1","bottomLeft":{"$id":"8","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"9","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"isLeaf":false,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"topRight":{"$id":"3","bottomLeft":{"$id":"6","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"7","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"isLeaf":false,"topLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"topRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"val":true},"val":true}

{

