class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        edge = {}

        for v in tickets:
            if v[0] in edge:
                edge[v[0]].append(v[1])
            else:
                edge[v[0]] = [v[1]]
            if v[1] not in edge: ####focus on this
                edge[v[1]]=[]

        for k in edge:
            edge[k].sort()
        print(edge)
        path=self.dfs(edge,"JFK",len(tickets),["JFK"])
        return path

    def dfs(self,edge,node,leftedge,tmp):
        print(node,edge)
        if leftedge==0:
            return tmp
        if len(edge[node])==0:
            return None
        else:
            # print(node)
            egs=edge[node]
            for i  in range(len(edge[node])):
                tmpe=edge[node][i]
                edge[node][i]=""
                tmp.append(tmpe)
                path= self.dfs(edge,tmpe,leftedge-1,tmp)
                if path is not None:
                    return path
                tmp.pop()
                edge[node][i]=tmpe
        return None

ticket=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

s=Solution()
print(s.findItinerary(ticket))




