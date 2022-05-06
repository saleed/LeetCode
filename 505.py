# coding:utf-8
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        dist=[[float("inf") for i in range(len(maze[0]))] for _ in range(len(maze))]
        dist[start[0]][start[1]]=0
        self.bfs(maze,(start[0],start[1]),(destination[0],destination[1]),dist)

        # for v in dist:
        #     print(v)
        d=dist[destination[0]][destination[1]]
        if d!=float("inf"):    # coding:utf-8
            return d
        else:
            return -1




    def dfs(self,maze,pos,dest,dist):
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        for i in range(4):
            x=pos[0]
            y=pos[1]
            step=0
            while not(x+dx[i]<0 or y+dy[i]<0 or x+dx[i]>=len(maze) or y+dy[i]>=len(maze[0]) or maze[x+dx[i]][y+dy[i]]==1):
                x=x+dx[i]
                y=y+dy[i]
                step+=1
            print(x,y)
            if  dist[x][y]>dist[pos[0]][pos[1]]+step:
                dist[x][y]=dist[pos[0]][pos[1]]+step
                self.dfs(maze,(x,y),dest,dist)

    ###BFS能够得到正确解答的前提是，最近距离的路径，转弯距离也最近
    def bfs(self,maze,start,dest,dist):
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        que=[start]
        while len(que)>0:
            pos=que[0]
            que=que[1:]


            for i in range(4):
                x=pos[0]
                y=pos[1]
                step=0
                while not(x+dx[i]<0 or y+dy[i]<0 or x+dx[i]>=len(maze) or y+dy[i]>=len(maze[0]) or maze[x+dx[i]][y+dy[i]]==1):
                    x=x+dx[i]
                    y=y+dy[i]
                    step+=1
                    # if (x,y)==dest:
                    #     return dist[pos[0]][pos[1]]+step

                if  dist[x][y]>dist[pos[0]][pos[1]]+step:
                    dist[x][y]=dist[pos[0]][pos[1]]+step
                    que.append((x,y))
        #
        for v in dist:
            print(v)
        return -1








test=[[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[3,2]]


maze=test[0]
start=test[1]
dest=test[2]

ss=Solution()
print(ss.shortestDistance(maze,start,dest))
for v in maze:
    print(v)