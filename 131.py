class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        huiwen=self.isHuiWen(s)

        res=[float("inf")]
        self.dfs(res,0,0,s,huiwen)
        return res[0]-1

    def isHuiWen(self,s):
        huiwen=[[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)):
                if i+j<len(s) and i-j>=0 and s[i+j]==s[i-j]:

                    huiwen[i-j][i+j]=True


                else:
                    break

            for j in range(len(s)):
                if i+j+1<len(s) and i-j>=0 and s[i+j+1]==s[i-j]:
                    huiwen[i-j][i+j+1]=True
                else:
                    break

        return huiwen


    def dfs(self,res,tmp,i,s,huiwen):
        # print(tmp,i)
        if i>=len(s):
            res[0]=min(res[0],tmp)
            return
        for p in range(i,len(s)):
            if huiwen[i][p]:
                self.dfs(res,tmp+1,p+1,s,huiwen)




a=Solution()
test="abba"
for v in a.isHuiWen(test):
    print(v)

print(a.partition(test))