class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """


        intervals.sort(key=lambda x:x[0])

        cnt=0
        res=[]
        for v in intervals:
            if len(res)==0:
                res.append(v)
            else:
                if v[0]<res[-1][1]:
                    if v[1]<res[-1][1]:
                        res.pop()
                        res.append(v)
                    cnt+=1
        return cnt