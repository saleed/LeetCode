class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        dp=["" for _ in range(k+1) ]
        for i in range(len(num)):
            dp[i][0]=num[:i+1]
        for j in range(1,k+1):
            dp[0][j]=""

        for i in range(1,len(num)):
            for j in range(1,k+1)[::-1]:
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+num[i])

        res=dp[len(num) - 1][k].lstrip('0')
        if res=="":
            return '0'
        else:
            return res


a=Solution()
num = "1432219"
k = 3

print(a.removeKdigits(num,k))

num = "10200"
k=1
print(a.removeKdigits(num,k))



test='00002000'
print(test.lstrip('0'))