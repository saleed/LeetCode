class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        gp={}
        for v in times:
            if v[0] in gp:
                gp[v[0]].append([v[1],v[2]])
            else:
                gp[v[0]]=[v[1],v[2]]

        return self.bfs(gp,n,k)





    def bfs(self,gp,n,k):

        ##其实是一个最短路问题，
        ##维护一个优先队列，需要从队列里每次找到距离源点最近的点
        ##需要使用优先队列 每个循环确定一个路径最小值 或者直接遍历

        dist = {}
        dist[k]=0
        vis=set()
        while True:
            mind=float("inf")
            selv=-1
            for v in dist:
                if v in vis:
                    continue
                if dist[v]<mind:
                    mind=dist[v]
                    selv=v
            if selv==-1:
                break
            vis.add(selv)
            for adj in gp[selv]:
                if adj[0] not in dist or mind+adj[1]<dist[adj[0]]:
                    dist[adj[0]]=mind+adj[1]

        if len(vis)<n:
            return -1
        maxv=0
        for k in dist:
            if maxv<dist[k]:
                maxv=dist[k]
        return maxv









