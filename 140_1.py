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
                    dp[i].append(j)

        print(dp)
        p=len(s)
        res=[]
        self.backtrack(dp,s,res,[],p)

        return res


    def backtrack(self,dp,s,res,tmp,p):
        if p<0:
            res.append(" ".join(list(reversed(tmp[:-1]))))
            return

        for v in dp[p]:
            tmp.append(s[v:p])
            self.backtrack(dp,s,res,tmp,v)
            tmp.pop()

a=Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(a.wordBreak(s,wordDict))



