class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sumv=int(n*(n+1)/2)


        dp=[[0 for _ in range(sumv+1)] for _ in range(n)]
        dp[0][0]=1
        for i in range(n):
            for j in range(int(i*(i+1)/2)+1):
                if j==0:
                    dp[i][j]=1
                else:
                    for kk in range(i):
                        if j-(i-kk)>=0:
                            dp[i][j]+=dp[i-1][j-(i-kk)]+1

            print(dp[i])
        return dp[-1][k]

ss=Solution()
n=3
k=1
print(ss.kInversePairs(n,k))

