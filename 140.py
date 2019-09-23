class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if len(s)==0 or len(wordDict)==0:
            return []
        dict=set(wordDict)


        dp=[False for _ in range(len(s)+1)]
        pre=[[] for _ in range(len(s)+1)]
        dp[0]=True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i]=True
                    pre[i].append(j)

        print(pre)
        if dp[len(s)]==True:
            path=self.generatePath(pre,s)
            # print(path)
            strres=[]
            for i in range(len(path)):
                path[i]=list(reversed(path[i]))
                strres.append(" ".join(path[i]))
            return strres
        # return dp[len(s)]

        return []
    def generatePath(self,pre,s):
        cur=len(s)
        res=[]
        self.recursiveSearch(res,pre,len(s),s,[])
        # strarr=[]
        # for i in res:
        #     strarr.append(" ".join(i))
        return res



    #回溯的方法？？
    def recursiveSearch(self,res,pre,id,s,curpath):
        if len(pre[id])==0:
            res.append(curpath[:])
            return
        for i in pre[id]:
            curpath.append(s[i:id])
            self.recursiveSearch(res,pre,i,s,curpath)
            curpath.pop()
a=Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(a.wordBreak(s,wordDict))

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(a.wordBreak(s,wordDict))


test=['pine', 'applepen', 'apple']
print(" ".join(test))