class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        huiwen=self.isHuiWen(s)
        res=[]
        self.dfs(s,0,huiwen,[],res)
        return res

    def isHuiWen(self,s):
        dp=[[i>=j for j  in range(len(s))] for i in range(len(s))]

        for itv in range(1,len(s)):
            for i in range(len(s)-1):
                if i+itv<len(s) and dp[i+1][i+itv-1] and s[i]==s[i+itv] :
                    dp[i][i+itv]=True
        print(dp)
        return dp


    def dfs(self,s,i,huiwen,tmp,res):
        if i>=len(s):
            res.append(tmp[:])
            return

        for j in range(i,len(s)):
            if huiwen[i][j]:
                tmp.append(s[i:j+1])
                self.dfs(s,j+1,huiwen,tmp,res)
                tmp.pop()


aaa=Solution()
s = "aab"
print(aaa.partition(s))





