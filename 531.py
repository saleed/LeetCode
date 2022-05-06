class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """

        rowdict=[[] for _ in range(len(picture))]
        coldict=[[] for _ in range(len(picture[0]))]
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=="W":
                    continue
                else:

                    rowdict[i].append(j)
                    coldict[j].append(i)
        cnt=0
        for i in range(len(picture)):
            if len(rowdict[i])==1 and len(coldict[rowdict[i][0]])==1:
                cnt+=1
        return cnt