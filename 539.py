class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        timePoints.sort()
        diff=float("inf")
        for i in range(1,len(timePoints)):
            time1=timePoints[i%len(timePoints)]
            time2=timePoints[(i-1)%len(timePoints)]
            hour1=int(time1[:2])
            hour2=int(time2[:2])
            minute1=int(time1[3:])
            minute2=int(time2[3:])
            diff=min(diff,((hour1-hour2)*60+minute1-minute2+(24*60))%(24*60))
        return diff
