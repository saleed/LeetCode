class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[0]
        self.dfs(n,0,0,0,res,"")
        return res[0]



    def dfs(self,n,absentday,continuelate,i,res,tmp):
        if i==n:
            res[0]+=1
            return
        if absentday<1:
            self.dfs(n,absentday+1,0,i+1,res,tmp+"A")
        if continuelate<2:
            self.dfs(n,absentday,continuelate+1,i+1,res,tmp+"L")
        self.dfs(n,absentday,0,i+1,res,tmp+"P")

    def dp(self,n):
        

