class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g={}
        dist={}
        for v in times:
            if v[0] not in g:
                g[v[0]]={}
            g[v[0]][v[1]]=v[2]

        print(g)

        dist={k:0}
        vis=set()
        while len(vis)<n:

