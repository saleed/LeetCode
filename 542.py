class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        zero=set()
        dist=[[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for i in range(len(mat)):
            for  j in range(len(mat[0])):
                if mat[i][j]==0:
                    zero.add((i,j))

        for i in range(len(mat)):
            for  j in range(len(mat[0])):
                if mat[i][j]==0:
                    dist[i][j]=0
                else:

                    for z in zero:
                        dist[i][j]=min(dist[i][j],abs(i-z[0])+abs(j-z[1]))
        return dist









    def bfs(self,i,j,mat,vis):
        if (i,j) in vis:
            return
        que=[(i,j)]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while len(que)>0:
            head=que[0]
            que=que[1:]
            for i in range(4):
                nx=head[0]+dx[i]
                ny=head[0]+dy[i]
                if 0<=nx<len(mat) and 0<=ny<len(mat[0]) and (nx,ny) not in vis and mat[nx][ny]==0:





