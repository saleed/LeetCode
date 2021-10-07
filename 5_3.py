#20210215

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


        ##一遍遍历的DP不知道怎么写
        # dp=[1]*len(s)
        # dp[0]=1
        # for i in range(1,len(s)):
        #     if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]==s[i]:
        #         dp[i]=dp[i-1]+2
        #     else:
        #
        # print(dp)
        #
        # max_len=0
        # max_idx=0
        # for i in range(len(dp)):
        #     if dp[i]>max_len:
        #         max_len=dp[i]
        #         max_idx=i
        # print(max_idx,max_len)
        #
        # return s[max_idx-max_len+1:max_idx+1]
        #


if __name__=="__main__":
    a=Solution()
    test="cccc"
    print(a.longestPalindrome(test))

