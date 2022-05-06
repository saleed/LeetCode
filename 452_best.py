class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        print(points)
        cnt=0
        rightbound=-float("inf")


        for p in points:
            if p[0]>rightbound:
                print(p)
                cnt+=1
                rightbound=p[1]
            else:
                rightbound=min(rightbound,p[1])
        return cnt



ss=Solution()
test=[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

print(ss.findMinArrowShots(test))