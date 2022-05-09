class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """

        l=0
        while n:
            l+=1
            n=n/10
        #
        # res = [0]
        # self.dfs(n, l, 0, 0, res)
        #
        # return res
        dp=[[0,0] for _ in range(l+1)]
        for i in range(1,l+1):
            dp[i][0]=dp[i-1][0]+dp[i-1][1]
            dp[i][1]=dp[i-1][0]





    def dpSolve(self,n,l):

        dp=[[0 for _ in range()]





    ##time limit exceeded


    def dfs(self,n,l,i,tmp,res):
        if i==l and tmp<=n:
            res[0]+=1
            return
        if i<l:
            if tmp%2==1:
                self.dfs(n,l,i+1,tmp*2,res)
            else:
                self.dfs(n,l,i+1,tmp*2+1,res)
                self.dfs(n,l,i+1,tmp*2,res)
