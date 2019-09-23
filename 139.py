class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s)==0 or len(wordDict)==0:
            return False
        dict=set(wordDict)

        dp=[False for _ in range(len(s)+1)]
        dp[0]=True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i]=True
                    break
        return dp[len(s)]

        # return self.dfs(s,dict)







    #超时
    def dfs(self,s,wordDict):
        # print(s,wordDict)
        if s=="":
            return True
        for i in wordDict:
            if len(i)<=len(s) and s[:len(i)]==i:
                if self.dfs(s[len(i):],wordDict):
                    return True
        return False


    def empty(self,dict):
        summ=0
        for val in dict.values():
            summ+=val
        return summ==0
a=Solution()

s = "leetcode"
wordDict = ["leet", "code"]

print(a.wordBreak(s,wordDict))



