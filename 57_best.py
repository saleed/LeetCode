class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=leftbound)

        res=[]
        for v in intervals:
            if len(res)==0:
                res.append(v)
            else:
                top=res[-1]
                if top[1]>=v[0]:
                    top[1]=max(v[1],top[1])
                    res[-1]=top
                else:
                    res.append(v)
        return res




def leftbound(x):
    return x[0]