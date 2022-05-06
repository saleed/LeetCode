class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        stickdict={}
        # for v in matchsticks:
        #     if v in stickdict:
        #         stickdict[v]+=1
        #     else:
        #         stickdict[v]=1
        l=sum(matchsticks)/4
        if sum(matchsticks)%4!=0:
            return False
        bucketLen={}
        matchsticks.sort()
        matchsticks=matchsticks[::-1]
        for i in range(4):
            bucketLen[i]=0
        return self.dfs(matchsticks,0,bucketLen,l)

    def dfs(self,matchsticks,i,bucketLen,bucketLimit):
        # print(bucketLen)
        if i==len(matchsticks):
            return True
        for j in range(4):
            if bucketLen[j]+matchsticks[i]>bucketLimit:
                continue
            bucketLen[j]+=matchsticks[i]
            if self.dfs(matchsticks,i+1,bucketLen,bucketLimit):
                return True
            bucketLen[j]-=matchsticks[i]
        return False


s=Solution()
test=[6122053,1031956,460065,3996684,3891947,1839190,6127621,8855952,8835594,3425930,4189081,7596722,876208,7952011,9676846]
print(s.makesquare(test))