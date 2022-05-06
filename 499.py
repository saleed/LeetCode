class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """

        res=self.bfs(maze,(ball[0],ball[1]),(hole[0],hole[1]),set())
        if res=="":
            return "impossible"
        return res
    def bfs(self,maze,ball,hole,vis):
        layer=[("",ball)]
        dx=[0,-1,1,0]
        dy=[1,0,0,-1]
        direction=["d","l","r","u"]
        while len(layer)>0:
            nextlayer=[]
            print(layer)
            for v in layer:
                vpath=v[0]
                for i in range(4):
                    nx=v[1][0]
                    ny=v[1][1]
                    while nx + dx[i]>=0 and ny + dy[i] >=0 and nx + dx[i]<len(maze) and ny + dy[i]<len(maze[0]) and maze[nx+dx[i]][ny+dy[i]]!=1:
                        nx+=dx[i]
                        ny+=dy[i]
                        if (nx,ny)==hole:
                            return vpath+direction[i]
                    if (nx,ny) in vis:
                        continue
                    else:
                        npath=vpath+direction[i]
                        nextlayer.append((npath,(nx,ny)))
                        vis.add((nx,ny))

            layer=nextlayer

        return ""



ss=Solution()
maze=[[0,0,0,0,0],
      [1,1,0,0,1],
      [0,0,0,0,0],
      [0,1,0,0,1],
      [0,1,0,0,0]]
start=[4,3]
end=[0,1]
print(ss.findShortestWay(maze,start,end))





