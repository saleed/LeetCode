class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        dp=[[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs))]

        maxv = -float("inf")
        if not (strs[0].count("0")>m or strs[0].count("1")>n):
            dp[0][strs[0].count("0")][strs[0].count("1")] = 1
            maxv=max(maxv, dp[0][strs[0].count("0")][strs[0].count("1")])


        for i in range(1,len(strs)):
            onecount=strs[i].count("1")
            zerocount=strs[i].count("0")
            print(onecount,zerocount)
            for mm in range(m+1):
                for nn in range(n+1):
                    zeronum=mm-zerocount
                    onenum=nn-onecount
                    if zeronum>=0 and onenum>=0:
                        dp[i][mm][nn]=max(dp[i-1][mm][nn],dp[i-1][zeronum][onenum]+1)
                    else:
                        dp[i][mm][nn]=dp[i-1][mm][nn]
                    maxv=max(maxv,dp[i][mm][nn])

        return maxv



# s="1030023"
# print(s.count("3"))

strs = ["10", "0001", "111001", "1", "0"]
m = 3
n = 4
ss=Solution()
print(ss.findMaxForm(strs,m,n))