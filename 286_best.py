class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # res=[[0 for _ in range(len(rooms[0]))] for _ in range(len(rooms))]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    self.bfs(rooms,i,j)

        # print(rooms)
        return rooms


    def bfs(self,rooms,x,y):
        que=[[x,y]]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        while len(que)>0:
            head=que[0]
            que=que[1:]
            tmpx=head[0]
            tmpy=head[1]
            print(tmpx,tmpy)
            for i in range(4):
                nx=tmpx+dx[i]
                ny=tmpy+dy[i]
                # print(rooms[tmpx][tmp)
                if 0<=nx<len(rooms) and 0<=ny<len(rooms[0]) and rooms[nx][ny]!=-1 and rooms[nx][ny]>rooms[tmpx][tmpy]+1:
                    rooms[nx][ny]=rooms[tmpx][tmpy]+1
                    que.append([nx,ny])

        return rooms



test=rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
#[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

s=Solution()
print(s.wallsAndGates(test))