class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # res = [0]
        # self.dfs(s, res)
        # return res[0]
        return self.dpSolve(s)

    def dfs(self, s, res):
        # print(s)
        if len(s)== 0:
            res[0]+=1
            return
        if '9' >= s[0] >= '1':
            self.dfs(s[1:], res)
        if len(s) > 1 and ((s[0] =='2' and '6' >= s[1] >= '0') or(s[0] =='1' and '9' >= s[1] >= '0')):
            self.dfs(s[2:], res)
        return


    def dpSolve(self,s):
        dp=[0]*len(s)
        dp[0]=0 if s[0]=='0' else 1

        if len(s)>1:
            if dp[0]==0:
                dp[1]=0
            else:
                if s[1]!='0':
                    dp[1]+=1
                if 26>=int(s[:2])>0:
                    dp[1]+=1
        for i in range(2,len(s)):
            if s[i]!='0' and dp[i-1]>0:
                dp[i]+=dp[i-1]
            if s[i-1]!='0' and 26>=int(s[i-1:i+1])>0 and dp[i-2]>0:
                dp[i]+=dp[i-2]

        print(dp)
        return dp[-1]


        #
        # n = len(s)
        # f = [1] + [0] * n
        # for i in range(1, n + 1):
        #     if s[i - 1] != '0':
        #         f[i] += f[i - 1]
        #     if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
        #         f[i] += f[i - 2]
        #
        # print(f)
        # return f[n]

    # [1, 2, 2, 4, 2, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12]
#  [1, 1, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4]
#

test="2611055971756562"
a=Solution()
print(a.numDecodings(test))




