class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edict = {}

        for v in edges:
            if v[0] in edict:
                edict[v[0]].append(v[1])
            else:
                edict[v[0]] = [v[1]]

            if v[1] in edict:
                edict[v[1]].append(v[0])
            else:
                edict[v[1]] = [v[0]]

        vis = set()
        cnt = 0
        for v in edict:

            if v not in vis:
                # print(v, vis)
                que = [v]
                while len(que) > 0:
                    head = que[0]
                    vis.add(head)
                    que = que[1:]
                    for vv in edict[head]:
                        if vv not in vis:
                            que.append(vv)
                cnt += 1

        cnt+=n-len(vis)

        return cnt



n=5
edge=[[0,1],[1,2],[3,4]]
s=Solution()
s.countComponents(n,edge)


