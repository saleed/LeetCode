# import queue
import heapq
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        return self.fixdp(dungeon)


    def dp(self,dungen):
        height=len(dungen)
        width=len(dungen[0])


        cost=[[-float("inf") for _ in range(width)] for _ in range(height)]
        vis=[[0 for _ in range(width)] for _ in range(height)]


        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        cost[0][0]=dungen[0][0]
        vis[0][0]=1
        tmp=0
        heap=[]






        ###求最短路径的错误方法
        while True:
            x=int(tmp/height)
            y=tmp%width
            mincost=float("inf")
            minid=[-1,-1]
            for i in range(4):
                newx=x+dx[i]
                newy=y+dy[i]
                if newx>=0 and newx<height and newy>=0 and newy<width and vis[newx][newy]==0:
                    if cost[newx][newy]<=cost[x][y]+dungen[newx][newy]:  ##使用这个松弛条件是求最短路
                        cost[newx][newy]=cost[x][y]+dungen[newx][newy]

                        ##这里错误，不是找当前节点所连接的节点的最小值，而是所有之前访问过的节点的最小值！！！
                    if cost[newx][newy]<mincost:
                        minid=[newx,newy]
            if not(minid[0]==-1 and minid[1]==-1):
                vis[minid[0]][minid[1]]=1
                tmp=minid[0]*height+minid[1]
            else:
                break

        return cost[height-1][width-1]



    def fixdp(self,dungen):
        height=len(dungen)
        width=len(dungen[0])


        cost=[[-float("inf") for _ in range(width)] for _ in range(height)]
        vis=[[0 for _ in range(width)] for _ in range(height)]


        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        cost[0][0]=dungen[0][0]
        vis[0][0]=1
        tmp=0

        while True:
            x=int(tmp/height)
            y=tmp%width
            # maxcost=-float("inf")
            # maxid=[-1,-1]
            for i in range(4):
                newx=x+dx[i]
                newy=y+dy[i]
                if newx>=0 and newx<height and newy>=0 and newy<width and vis[newx][newy]==0:
                    if dungen[newx][newy]>=0:  ##使用这个松弛条件
                        cost[newx][newy]=max(cost[x][y],cost[newx][newy])
                    else:
                        cost[newx][newy]=max(cost[x][y]+dungen[newx][newy],cost[newx][newy])
            x,y=self.getNextMinNode(cost,vis)
            if x==-1 and y==-1:
                break
            else:
                vis[x][y]=1
                tmp=x*height+y
        print(cost)

        return cost[height-1][width-1]

    def getNextMinNode(self,cost,vis):
        maxv=-float("inf")
        x=-1
        y=-1
        for i in range(len(vis)):
            for j in range(len(vis[0])):
                if vis[i][j]==0 and maxv<cost[i][j]:
                    maxv=cost[i][j]
                    x=i
                    y=j
        return x,y

        # 以上的求解没看清题目，题目上已经明显指出每次只能往下或者向右移动


a=Solution()
d=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(a.calculateMinimumHP(d))





print("##################")
heap=[1,3,6,9,0]
heapq.heapify(heap)
print(heapq.heappop(heap))