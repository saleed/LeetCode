class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        edgedict={}
        for v in wall:
            start=0
            for w in v:
                if w+start in edgedict:
                    edgedict[w+start]=edgedict[w+start]+1
                else:
                    edgedict[w+start]=1
                start+=w
        maxv=0
        print(edgedict)
        print(sum(wall[0]))
        for k in edgedict:
            if k==sum(wall[0]):
                continue
            elif maxv<edgedict[k]:
                maxv=edgedict[k]
        return len(wall)-maxv


test=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
ss=Solution()
print(ss.leastBricks(test))