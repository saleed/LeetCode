class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # res=[0]
        # self.dfs(coins,0,amount,res)
        # return res[0]
        #
        return self.dpSolve(coins,amount)




    def dfs(self,coins,i,left,res):
        if left==0:
            res[0]+=1
            return
        if i<len(coins):
            n=0
            while left-n*coins[i]>=0:
                self.dfs(coins,i+1,left-n*coins[i],res)
                n+=1

    def dpSolve(self,coins,amount):
        dp=[[ 0 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount+1):
                if i==0:
                    dp[i][j]=1 if j%coins[i]==0 else 0
                else:
                    n=0
                    while j-n*coins[i]>=0:
                        dp[i][j]+=dp[i][j-n*coins[i]]
        return dp[-1][-1]
