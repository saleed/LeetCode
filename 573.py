class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """

        treeNutDist=[]
        for i in range(len(nuts)):
            treeNutDist.append(abs(nuts[i][0]-tree[0])+abs(nuts[i][1]-tree[1]))
        mindist=float("inf")
        sumdist=sum(treeNutDist)*2
        for i in range(len(nuts)):
            mindist=min(mindist,sumdist-treeNutDist[i]+abs(squirrel[0]-nuts[i][0])+abs(squirrel[1]-nuts[i][1]))
        return mindist
