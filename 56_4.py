class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=rightbound)

        res=[intervals[0]]
        for v in intervals[1:]:
            if v[0]<=res[-1][1]:
                res[-1][1]=max(v[1],res[-1][1])
            else:
                res.append(v)
        return res




def rightbound(x):
    return x[0]

intervals = [[1,3],[2,6],[8,10],[15,18]]
a=Solution()
print(a.merge(intervals))
