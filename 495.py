class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        intv=[]
        for t in timeSeries:
            intv.append([t,t+duration])

        res=0
        tmp=[]
        for v in intv:
            if len(tmp)==0:
                tmp=v
            else:
                if v[0]<=tmp[1]:
                    tmp[1]=v[1]
                else:
                    res+=tmp[1]-tmp[0]+1
                    tmp=v
        res+=tmp[1]-tmp[0]+1
        return res
