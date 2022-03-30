class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        ##backtrack + dp

        dp=[[] for _ in range(len(s)+1)]
        dp[0]=[-1]
        for i in range(1,len(s)+1):
            for j in range(i):
                if len(dp[j])>0 and s[j:i] in wordDict:
                    print(i,j)
                    dp[i].append(j)
        #print(dp)
        res=[]
        self.backTrack(dp,s,len(s),[],res)
        return res

    def backTrack(self,dp,s,i,tmp,res):
        if i<=0:
            res.append(" ".join(tmp[:][::-1]))
            return
        if len(dp[i])>0:
            for v in dp[i]:
                tmp.append(s[v:i])
                self.backTrack(dp,s,v,tmp,res)
                tmp.pop()




a="catsanddog"
t=["cat","cats","and","sand","dog"]

s=Solution()
print(s.wordBreak(a,t))