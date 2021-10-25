class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle==None or len(triangle)==0:
            return 0
        res=[0]*len(triangle)
        res[0]=triangle[0][0]
        for row in range(1,len(triangle)):
            print(res)
            for i in reversed(range(len(triangle[row]))):
                res[i] = (triangle[row][i] + min(res[i - 1] if i - 1 >= 0 else float("inf"),
                                                 res[i] if i < row else float("inf")))
        return min(res)

a=Solution()
test=[[2],[3,4],[6,5,7],[4,1,8,3]]
print(a.minimumTotal(test))



