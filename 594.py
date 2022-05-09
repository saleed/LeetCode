class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        vdict={}
        for v in nums:
            vdict[v]=1 if v not in vdict else vdict[v]+1
        res=0
        for k in vdict:
            if k+1 in vdict:
                res=max(res,vdict[k]+vdict[k+1])
        return res