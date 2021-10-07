
##对区间的排序，
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        if len(intervals)==0:
            return 0
        res=intervals[0]
        for intv in intervals:
            if intv[0]>res[-1][1]:
                res.append(intv)
            else:
                res[-1][1]=max(res[-1][1],intv[1])
        return res