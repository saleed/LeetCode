class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # dist={}
        # for i in range(len(maze)):
        #     for j in range(len(maze[0])):
        #         if i==0 or j==0 or i==len(maze)-1 or j==len(maze[0])-1:
        #             dist[(i,j)]=float("inf")
        vis=set()
        return self.dfs(maze,(start[0],start[1]),(destination[0],destination[1]),vis)


    def dfs(self,maze,pos,destation,vis):
        if pos in vis:
            return False

        if pos==destation:
            return True

        x=pos[0]
        y=pos[1]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        vis.add(pos)
        for i in range(4):
            tmpx=x
            tmpy=y
            while not( tmpx+dx[i]<0 or tmpy+dy[i]<0
                or tmpx+dx[i]==len(maze) or tmpy+dy[i]==len(maze[0])) and maze[tmpx+dx[i]][tmpy+dy[i]]==0:

                tmpx+=dx[i]
                tmpy+=dy[i]

            if self.dfs(maze,(tmpx,tmpy),destation,vis):
                return True
        return False




ss=Solution()
maze=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start=[0,4]
dest=[1,2]
for v in maze:
    print(v)

print(ss.hasPath(maze,start,dest))