class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sdict={}
        res=[]
        sortscore=score[:]
        sortscore.sort()
        cnt=1
        for s in sortscore[::-1]:
            sdict[s]=cnt
            cnt+=1
        for v in score:
            if sdict[v]==1:
                res.append("Gold Medal")
            elif sdict[v]==2:
                res.append("Silver Medal")
            elif sdict[v] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(sdict[v]))
        return res
