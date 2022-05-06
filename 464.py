class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        state=0
        dp={}
        leftspace=0
        for i in range(1,maxChoosableInteger+1):
            leftspace+=i
        self.dfs(state,dp,0,desiredTotal,maxChoosableInteger,leftspace)
        return dp[0]

    def dfs(self,state,dp,tmpsum,desire,maxChoosableInteger,leftspace):

        if state in dp:
            return

        if leftspace<desire:
            dp[state]=False
            return

        for i in range(maxChoosableInteger)[::-1]:
            if (1<<i)&state==0:
                if i+1>=desire:
                    dp[state]=True
                    return
                else:
                    newstate=(1<<i)|state
                    self.dfs(newstate,dp,tmpsum+i,desire-i,maxChoosableInteger,leftspace-i)
                    if dp[newstate]:
                        dp[state]=True
        if state not in dp:
            dp[state]=False

maxn=10
desire=11
ss=Solution()
print(ss.canIWin(maxn,desire))